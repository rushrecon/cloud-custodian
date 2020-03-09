VERSIONS_TEMPLATE = """

_versions = {%s}

def setup_version(name):
  if name not in _versions:
    fail('Could not find setup version: '  + name)
  return _versions[name]

"""

GET_VERSION_FROM_SETUP_PY = """
grep -oP \"'fallback_version': \K'.*?'\"
"""

def _create_version_py(ctx):
    b = ctx.execute(["grep", "-oP", "'fallback_version': \K'.*?'", "setup.py"]).stdout
    ctx.file("version.py", "version = u%s" % b)
    ctx.file("BUILD.bazel", "\n")

def create_versions_bzl(ctx):
    versions = []
    for setup_file_name in ctx.attr.setup_files:
        ctx.file("tmp", content = ctx.read(setup_file_name))
        version = ctx.execute(["grep", "-oP", "version=\K'.*'", "tmp"]).stdout.strip()
        versions.append("\"%s\":%s" % (setup_file_name, version))
    return VERSIONS_TEMPLATE % ",".join(versions)

def _hello_repo_impl(ctx):
    ctx.file("BUILD.bazel", 'exports_files(["hello.txt"])')
    ctx.file("versions.bzl", create_versions_bzl(ctx))
    ctx.file("BUILD.bazel", "")

setup_versions_repository = repository_rule(
    implementation = _hello_repo_impl,
    local = False,
    attrs = {
        "setup_files": attr.label_list(allow_files = True),
    },
)
