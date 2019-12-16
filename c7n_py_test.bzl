load("@rules_python//python:defs.bzl", "py_library", "py_test")

def _impl(ctx):
    old_runner = ctx.attr.test[DefaultInfo].files_to_run.executable
    new_runner = ctx.actions.declare_file(ctx.attr.name)

    ctx.actions.run_shell(
        progress_message = 'Patching file content - %s' % old_runner.short_path,
        # TODO: replace all *.inner mentions in file_to_run
        command ="sed $'s/" +
            "  args = \[python_program, main_filename\] + args/" + # search string
            "  os.chdir(os.path.join(module_space, \"__main__\"))\\\n" + # replacing strings
            "  module_name = \"'%s'.'%s'\"\\\n" % (ctx.label.package.replace("/", "."), ctx.attr.name) +
            "  args = \[python_program, \"-m\", \"unittest\", module_name\] + args/g'" +
            " '%s' > '%s' " % (old_runner.path, new_runner.path),
        inputs = [old_runner],
        outputs = [new_runner],
    )

    return [DefaultInfo(
        runfiles = ctx.attr.test.default_runfiles,
        executable = new_runner,
    )]

_py_test = rule(
    implementation = _impl,
    executable = True,
    attrs = {
        "test": attr.label(mandatory = True),
    },
    test = True,
)

def c7n_py_test(name, **kwargs):
    inner_test_name = name + ".inner"
    kwargs.update(main = name + ".py", tags = ["manual"])
    py_test(name = inner_test_name, **kwargs)
    _py_test(name = name, test = inner_test_name)