# template for generating bzl-file
VERSIONS_TEMPLATE = """

_versions = {%s}

def setup_version(name):
  if name not in _versions:
    fail('Could not find setup version: '  + name)
  return _versions[name]

"""

def create_versions_bzl(ctx):
    versions = []
    for setup_file_name in ctx.attr.setup_files:
        ctx.file("tmp", content = ctx.read(setup_file_name))
        version = ctx.execute(["grep", "-oP", "'version': \K'.*'", "tmp"]).stdout.strip()
        versions.append("\"%s\":%s" % (setup_file_name, version))
    return VERSIONS_TEMPLATE % ",".join(versions)

def _version_repo_impl(ctx):
    ctx.file("versions.bzl", create_versions_bzl(ctx))
    ctx.file("BUILD.bazel", "")

setup_versions_repository = repository_rule(
    implementation = _version_repo_impl,
    local = False,
    attrs = {
        "setup_files": attr.label_list(allow_files = True),
    },
)
