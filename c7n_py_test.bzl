load("@rules_python//python:defs.bzl", "py_library", "py_test")

def _impl(ctx):
    if ctx.configuration.coverage_enabled:
        my_out = ctx.outputs.executable
        ctx.actions.write(
            content = "cd /home/polina/cloud-custodian; pytest -n auto --cov tests --cov-report html --cov-append tests/{0}.py; cd -;".format(ctx.attr.name),
            output = my_out,
            is_executable = True,
        )
        return [DefaultInfo(executable = my_out)]
    else:
        old_runner = ctx.attr.test[DefaultInfo].files_to_run.executable
        new_runner = ctx.actions.declare_file(ctx.attr.name)

        ctx.actions.run_shell(
            progress_message = "Patching file content - %s" % old_runner.short_path,
            # TODO: replace all *.inner mentions in file_to_run
            command = " echo '-------------------Hi, I am executing!!!!!';sed $'s/" +
                      "  args = \[python_program, main_filename\] + args/" +  # search string
                      "  os.chdir(os.path.join(module_space, \"__main__\"))\\\n" +  # replacing strings
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
        "srcs": attr.label_list(allow_files = True),
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

#def _c7n_py_cov_test_impl(ctx):
#    my_out = ctx.outputs.executable
#    ctx.actions.run_shell(
#        command = "echo 'cd /home/polina/cloud-custodian; /home/polina/cloud-custodian/.tox/py36-cov/bin/py.test -n auto --cov tests --cov-report html tests; cd -;' > {0}".format(my_out.path),
#        outputs = [my_out],
#    )
#
#    return [DefaultInfo(executable = my_out)]
#
#c7n_py_cov_test = rule(
#    implementation = _c7n_py_cov_test_impl,
#    executable = True,
#    test = True,
#)
