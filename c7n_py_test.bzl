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
    test_name = ctx.attr.name
    test_pkg = ctx.label.package.replace("/", ".")
    command = ""

    if ctx.configuration.coverage_enabled:
        command = (
            "  os.system(\"mkdir \" + os.path.join(os.getenv(\"TMPDIR\"), \"C7N-cov\"))\\\n" +
            "  os.system(\"mkdir \" + os.path.join(os.getenv(\"TMPDIR\"), \"C7N-cov\", \"%s\"))\\\n" % (test_pkg) +
            "  while len(os.path.basename(os.getcwd())) != 32:\\\n" +
            "    os.chdir(\"..\")\\\n" +
            "  os.chdir(os.path.join(\"execroot\", \"%s\"))\\\n" % (ctx.workspace_name) +
            "  os.environ[\"COVERAGE_FILE\"] = os.path.join(os.getenv(\"TMPDIR\"), \"C7N-cov\", \"%s\", \".coverage\")\\\n" % (test_pkg) +
            "  args = \[python_program, \"-m\", \"coverage\", \"run\", \"--rcfile\", \".bazel-coveragerc\", \"-m\", \"unittest\", \"%s.%s\"\] + args" % (test_pkg, test_name)
        )
    else:
        command = (
            "  os.chdir(os.path.join(module_space, \"%s\"))\\\n" % (ctx.workspace_name) +
            "  args = \[python_program, \"-m\", \"unittest\", \"%s.%s\"\] + args" % (test_pkg, test_name)
        )

    ctx.actions.run_shell(
        progress_message = "Patching file content - %s" % old_runner.short_path,
        # TODO: replace all *.inner mentions in file_to_run
        command =
            "sed $'s/" +
            "  args = \[python_program, main_filename\] + args/" + command +
            " /g' '%s' %s > '%s'" % (old_runner.path, excluded_pkgs_command, new_runner.path),
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
