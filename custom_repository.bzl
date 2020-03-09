BUILD_TEMPLATE = """

def a():
    print('kek')

"""

BUILD_TEMPLATE2 = '''
\n
package(default_visibility = ["//visibility:public"])

exports_files(["c7n/version.py"])
load("@rules_python//python:defs.bzl", "py_library")

#py_library(
#    name = "version",
#    srcs = [
#        "c7n/version.py",
#    ],
#)




'''

GET_VERSION_FROM_SETUP_PY = """
grep -oP \"'fallback_version': \K'.*?'\"
"""

def _create_version_py(ctx):
    b = ctx.execute(["grep", "-oP", "'fallback_version': \K'.*?'", "setup.py"]).stdout
    ctx.file("c7n/version.py", "version = u%s" % b)
    ctx.file("BUILD.bazel", "\n")

def _hello_repo_impl(ctx):
    ctx.file("hello.txt", ctx.attr.message)
    ctx.file("BUILD.bazel", 'exports_files(["hello.txt"])')
    ctx.file("kek.bzl", BUILD_TEMPLATE)
    ctx.file("setup.py", content = ctx.read(ctx.attr.setup_file))
    _create_version_py(ctx)
    ctx.file("BUILD.bazel", BUILD_TEMPLATE2)

hello_repo = repository_rule(
    implementation = _hello_repo_impl,
    local = False,
    attrs = {
        "message": attr.string(
            mandatory = True,
        ),
        "setup_file": attr.label(allow_single_file = True),
    },
)
