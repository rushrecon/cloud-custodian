load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_federation",
    sha256 = "506dfbfd74ade486ac077113f48d16835fdf6e343e1d4741552b450cfc2efb53",
    url = "https://github.com/bazelbuild/bazel-federation/releases/download/0.0.1/bazel_federation-0.0.1.tar.gz",
)

load("@bazel_federation//:repositories.bzl", "rules_python_deps")

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

load("@rules_python//python:pip.bzl", "pip3_import", "pip_repositories")

pip_repositories()

#=== Install pip deps for core part ====
pip3_import(
    name = "core_pip_deps",
    requirements = "//:requirements-bazel-dev.txt",
)

load("@core_pip_deps//:requirements.bzl", "pip_install")

pip_install()

#=== Install pip deps for GCP part ====
pip3_import(
    name = "gcp_pip_deps",
    requirements = "//tools/c7n_gcp:requirements.txt",
)

load("@gcp_pip_deps//:requirements.bzl", "pip_install")

pip_install()

#=== Install pip deps for core part ====
pip3_import(
    name = "pip_deps",
    requirements = "//:requirements-bazel-dev.txt",
)

load("@pip_deps//:requirements.bzl", "pip_install")

pip_install()

#
local_repository(
    name = "c7n",
    path = "c7n",
)

local_repository(
    name = "c7n_gcp",
    path = "tools/c7n_gcp/c7n_gcp",
)
