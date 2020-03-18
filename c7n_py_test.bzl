load("@rules_python//python:defs.bzl", "py_library", "py_test")

def add_exclude_pkgs_command(excluded_pkgs):
    """If there are excluded packages, add extra sed command to exclude these pkges from runfile"""
    if excluded_pkgs == []:
        return ""
    excluded_pkgs = ["\"__%s\"" % i.replace("-", "_").replace(".", "_") for i in excluded_pkgs]
    excluded_pkgs = "[%s]" % ",".join(excluded_pkgs)
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

    test_name = ctx.attr.name  # '\",\"'.join(package.split("/"))
    package_name = ctx.label.package.replace("/", ".")
    module_name = "%s.%s" % (package_name, test_name)
    cov_dir = "C7N-cov"

    command = ("sed $'s/" +
               # search string
               "  args = \[python_program, main_filename\] + args/" +
               # replacing strings
               "  module_name = \"%s\"\\\n" % (module_name) +
               "  os.chdir(os.path.join(module_space, \"%s\"))\\\n" % (ctx.workspace_name) +
               "  os.system(\"mkdir \" + os.path.join(os.getenv(\"TMPDIR\"), \"%s\"))\\\n" % (cov_dir) +
               "  os.system(\"mkdir \" + os.path.join(os.getenv(\"TMPDIR\"), \"%s\", \"%s\"))\\\n" % (cov_dir, package_name) +
               "  os.environ[\"COVERAGE_FILE\"] = os.path.join(os.getenv(\"TMPDIR\"), \"%s\", \"%s\", \".coverage\")\\\n" % (cov_dir, package_name) +
               "  args = \[python_program, \"-m\", \"coverage\", \"run\"," +
               "  \"--source\", os.getenv(\"C7N\"), \"--omit\", \"*\/tests\/*,*\/.*\/*\", \"--parallel-mode\"," +
               "  \"-m\", \"unittest\", module_name\] + args/g'" +
               " '%s' %s > '%s'" % (old_runner.path, excluded_pkgs_command, new_runner.path))
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
