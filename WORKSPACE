# https://docs.bazel.build/versions/0.19.1/be/workspace.html#http_archive
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

# https://github.com/bazelbuild/rules_python
git_repository(
    name = "rules_python",
    commit = "94677401bc56ed5d756f50b441a6a5c7f735a6d4",
    remote = "https://github.com/bazelbuild/rules_python",
    shallow_since = "1573842889 -0500",
#    sha256 = "aa96a691d3a8177f3215b14b0edc9641787abaaa30363a080165d06ab65e1161",
)

load("@rules_python//python:repositories.bzl", "py_repositories")

py_repositories()

load("@rules_python//python:pip.bzl", "pip_repositories")

pip_repositories()

load("@rules_python//python:pip.bzl", "pip3_import")

pip3_import(
    name = "pip_deps",
    requirements = "//:requirements-bazel-dev.txt",
)

load("@pip_deps//:requirements.bzl", "pip_install")

pip_install()

local_repository(
    name = "c7n",
    path = "c7n",
)

local_repository(
    name = "c7n_gcp",
    path = "tools/c7n_gcp/c7n_gcp",
)
