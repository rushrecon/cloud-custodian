load("@rules_python//python:defs.bzl", "py_library", "py_test")

def _impl(ctx):
    old_runner = ctx.attr.test[DefaultInfo].files_to_run.executable
    new_runner = ctx.actions.declare_file(ctx.attr.name)

    ctx.actions.run_shell(
        progress_message = "Patching file content - %s" % old_runner.short_path,
        # TODO: replace all *.inner mentions in file_to_run
        command = " sed $'s/" +
                  # search string
                  "  args = \[python_program, main_filename\] + args/" +
                  # replacing strings
                  "  os.chdir(os.path.join(module_space, \"__main__\"))\\\n" +
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
    tags = kwargs.pop("tags", default = [])
    main_name = kwargs.pop("name", default = name + ".py")
    kwargs.update(main = main_name, tags = tags + ["manual"])
    py_test(name = inner_test_name, **kwargs)
    _py_test(name = name, tags = tags, test = inner_test_name)

def _c7n_py_cov_impl(ctx):
    my_out = ctx.outputs.executable
    ctx.actions.write(
        content = "cd $C7N; pytest -n auto --cov-report html --cov-append --cov tests {}; cd -".format(" ".join([f.path for f in ctx.files.srcs])),
        output = my_out,
        is_executable = True,
    )

    return [DefaultInfo(executable = my_out)]

c7n_py_cov = rule(
    implementation = _c7n_py_cov_impl,
    attrs = {
        "srcs": attr.label_list(allow_files = True),
    },
    executable = True,
)
