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
            #  save coverage data to /tmp/C7N-cov/[test.module]/
            "  cov_path = os.path.join(os.getenv(\"TMPDIR\"), \"C7N-cov\", \"%s\")\\\n" % (test_pkg) +
            "  os.system(\"mkdir -p \" + cov_path)\\\n" +
            #  target dir: /home/user/.cache/bazel/_bazel_user/hash of the workspace dir/execroot/__main__
            "  while not re.match(\"[a-zA-Z0-9]{32}\", os.path.basename(os.getcwd())):\\\n" +
            "    os.chdir(\"..\")\\\n" +
            "  os.chdir(os.path.join(\"execroot\", \"%s\"))\\\n" % (ctx.workspace_name) +
            "  os.environ[\"COVERAGE_FILE\"] = os.path.join(cov_path, \".coverage\")\\\n" +
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


"""
We have a lot of tests of AWS, and to fit GitHub Actions worker limits,
it's splitted for chunks, which is rougly equal in processing time and
resource consumption.
This function just goes through the list and divide it by test name.
"""
def get_chunk(test_file_name):
    if test_file_name < "test_dynamodb":
        return "first_chunk"
    elif test_file_name < "test_iam":
        return "second_chunk"
    elif test_file_name < "test_redshift":
        return "third_chunk"
    else:
        return "fourth_chunk"
