# https://docs.bazel.build/versions/0.19.1/be/workspace.html#http_archive
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# https://github.com/atlassian/bazel-tools/tree/master/multirun
http_archive(
    name = "com_github_atlassian_bazel_tools",
    strip_prefix = "bazel-tools-b69e7d9844d1aa4908c5cb445fdba78a8932e4c6",
    urls = ["https://github.com/atlassian/bazel-tools/archive/b69e7d9844d1aa4908c5cb445fdba78a8932e4c6.tar.gz"],
)

load("@com_github_atlassian_bazel_tools//:multirun/deps.bzl", "multirun_dependencies")

multirun_dependencies()

# https://github.com/bazelbuild/rules_python
http_archive(
    name = "rules_python",
    sha256 = "aa96a691d3a8177f3215b14b0edc9641787abaaa30363a080165d06ab65e1161",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.0.1/rules_python-0.0.1.tar.gz",
)

load("@rules_python//python:repositories.bzl", "py_repositories")

py_repositories()

load("@rules_python//python:pip.bzl", "pip_repositories")

pip_repositories()

load("@rules_python//python:pip.bzl", "pip_import")

pip_import(
    name = "my_deps",
    requirements = "//:requirements-bazel-dev.txt",
)

pip_import(
    name = "my_deps_gcp",
    requirements = "//tools/c7n_gcp:requirements.txt",
)

load("@my_deps//:requirements.bzl", "pip_install")

pip_install()

load("@my_deps_gcp//:requirements.bzl", "pip_install")

pip_install()

local_repository(
    name = "c7n",
    path = "c7n",
)

local_repository(
    name = "c7n_gcp",
    path = "tools/c7n_gcp/c7n_gcp",
)
