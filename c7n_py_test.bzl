load("@rules_python//python:defs.bzl", "py_library", "py_test")

def add_exclude_pkgs_command(excluded_pkgs):
    """If there are excluded packages, add extra sed command to exclude these pkges from runfile"""
    if excluded_pkgs == []:
        return ""
    excluded_pkgs = ["\"__%s\"" % i.replace("-", "_").replace(".", "_") for i in excluded_pkgs]
    excluded_pkgs = "[%s]" % ",".join(excluded_pkgs)
    print(excluded_pkgs)
    exclude_pkgs_command = \
        "| sed $'s/" + \
        "  python_path_entries = \[GetWindowsPathWithUNCPrefix(d) for d in python_path_entries\]/" + \
        "  python_path_entries = [GetWindowsPathWithUNCPrefix\(d\)" + \
        " for d in python_path_entries if not list\(filter\(d.endswith, %s\)\)]/g'" % excluded_pkgs
    return exclude_pkgs_command

def _impl(ctx):
    old_runner = ctx.attr.test[DefaultInfo].files_to_run.executable
    new_runner = ctx.actions.declare_file(ctx.attr.name)
    excluded_pkgs_command = add_exclude_pkgs_command(ctx.attr.excluded_pkgs)
    package = ctx.label.package
    test_name = ctx.attr.name  # '\",\"'.join(package.split("/"))

    command = ("sed $'s/" +
               "  args = \[python_program, main_filename\] + args/" +  # search string
               # replacing strings
               "  os.chdir(os.getenv(\"C7N\"))\\\n" +
               "  module_name = os.path.join(\"%s\", \"%s.py\")\\\n" % (package, test_name) +  # relative path to test: tests/test_cli.py
               "  os.system(\"mkdir \/tmp\/C7N-cov; mkdir \/tmp\/C7N-cov\/%s\")\\\n" % (package.replace("/", "_")) +  # make temp dirs to store reports and test results
               "  os.environ\[\"COVERAGE_FILE\"\] = os.path.join(os.getenv(\"TMPDIR\"), \"C7N-cov\", \"%s\", \".coverage\")\\\n" % (package.replace("/", "_")) +
               "  args = \[python_program, \"-m\", \"pytest\", \"-n\", \"auto\"," +
               "  \"--cov-report\", \"html:\" + os.path.join(os.getenv(\"TMPDIR\"), \"C7N-cov\", \"%s\", \"html\")," % (package.replace("/", "_")) +
               "  \"--junitxml\", os.path.join(os.getenv(\"TMPDIR\"), \"C7N-cov\", \"%s\", \"test-results.xml\"), \"--cov\", \"\/\", \"--cov-config\", \".coveragerc\", module_name\] + args\\\n" % (package.replace("/", "_")) +
               "  /g'" +
               " '%s' %s > '%s'" % (old_runner.path, excluded_pkgs_command, new_runner.path))
    print(command)
    if ctx.configuration.coverage_enabled:
        ctx.actions.run_shell(
            command = command,
            inputs = [old_runner],
            outputs = [new_runner],
        )
    else:
        ctx.actions.run_shell(
            progress_message = "Patching file content - %s" % old_runner.short_path,
            # TODO: replace all *.inner mentions in file_to_run
            command = "sed $'s/" +
                      "  args = \[python_program, main_filename\] + args/" +  # search string
                      "  os.chdir(os.path.join(module_space, \"__main__\"))\\\n" +  # replacing strings
                      "  module_name = \"'%s'.'%s'\"\\\n" % (ctx.label.package.replace("/", "."), ctx.attr.name) +
                      "  args = \[python_program, \"-m\", \"unittest\", module_name\] + args/g'" +
                      " '%s' %s > '%s'" % (old_runner.path, excluded_pkgs_command, new_runner.path),
            inputs = [old_runner],
            outputs = [new_runner],
        )

    return [DefaultInfo(
        runfiles = ctx.attr.test.default_runfiles,
        executable = new_runner,
    )]

#"  args = \[python_program, \"-m\", \"py.test\" , \"--cov-report\", \"html\", \"--cov\", \"\/home\/polina\/cloud-custodian\/tests\", \"\/home\/polina\/cloud-custodian\/\" + module_name + \".py\"] + args\\\n  print(args)/g'" +

_py_test = rule(
    implementation = _impl,
    executable = True,
    attrs = {
        "test": attr.label(mandatory = True),
        "excluded_pkgs": attr.string_list(default = []),
    },
    test = True,
)

def c7n_py_test(name, **kwargs):
    inner_test_name = name + ".inner"
    tags = kwargs.pop("tags", default = [])
    main_name = kwargs.pop("name", default = name + ".py")
    excluded_pkgs = kwargs.pop("excluded_pkgs", default = [])
    kwargs.update(main = main_name, tags = tags + ["manual"])
    py_test(name = inner_test_name, **kwargs)
    _py_test(name = name, tags = tags, test = inner_test_name, excluded_pkgs = excluded_pkgs)

#def _c7n_py_cov_impl(ctx):
#    my_out = ctx.outputs.executable
#    ctx.actions.write(
#        content = "cd $C7N; pytest -n auto --cov-report html --cov-append --cov tests {}; cd -".format(" ".join([f.path for f in ctx.files.srcs])),
#        output = my_out,
#        is_executable = True,
#    )
#
#    return [DefaultInfo(executable = my_out)]
#
#c7n_py_cov = rule(
#    implementation = _c7n_py_cov_impl,
#    attrs = {
#        "srcs": attr.label_list(allow_files = True),
#    },
#    executable = True,
#)
