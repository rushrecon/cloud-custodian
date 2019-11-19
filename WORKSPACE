# https://docs.bazel.build/versions/0.19.1/be/workspace.html#http_archive
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

# https://github.com/atlassian/bazel-tools/tree/master/multirun
http_archive(
    name = "com_github_atlassian_bazel_tools",
    strip_prefix = "bazel-tools-b69e7d9844d1aa4908c5cb445fdba78a8932e4c6",
    urls = ["https://github.com/atlassian/bazel-tools/archive/b69e7d9844d1aa4908c5cb445fdba78a8932e4c6.tar.gz"],
)

load("@com_github_atlassian_bazel_tools//:multirun/deps.bzl", "multirun_dependencies")

multirun_dependencies()

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

load("@rules_python//python:pip.bzl", "pip_import", "pip3_import")

pip3_import(
    name = "my_deps",
    requirements = "//:requirements-bazel-dev.txt",
)

pip3_import(
    name = "my_deps_gcp",
    requirements = "//tools/c7n_gcp:requirements.txt",
)

load("@my_deps//:requirements.bzl", pip_install_base = "pip_install")

pip_install_base()

load("@my_deps_gcp//:requirements.bzl", pip_install_gcp = "pip_install")

pip_install_gcp()

local_repository(
    name = "c7n",
    path = "c7n",
)

local_repository(
    name = "c7n_gcp",
    path = "tools/c7n_gcp/c7n_gcp",
)
