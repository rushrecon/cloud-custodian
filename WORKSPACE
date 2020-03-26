load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
load("//:setup_versions_repository.bzl", "setup_versions_repository")

# https://github.com/bazelbuild/rules_python
git_repository(
    name = "rules_python",
    commit = "7879ef37d6cd1248143c7cba39ce4e6efaefbe60",
    remote = "https://github.com/alexkarpitski/rules_python",
    shallow_since = "1584368888 +0300",
)

load("@rules_python//python:repositories.bzl", "py_repositories")

py_repositories()

load("@rules_python//python:pip.bzl", "pip3_import", "pip_repositories")

pip_repositories()

pip3_import(
    name = "pip_deps",
    requirements = "//:requirements-bazel-dev.txt",
)

load("@pip_deps//:requirements.bzl", "pip_install")

pip_install()

# pip_import / requirement() does not work for the pypi azure package, therefore we use rules_python_external rules
# See issue: https://github.com/bazelbuild/rules_python/issues/273
git_repository(
    name = "rules_python_external",
    commit = "95e72ceda4d1edaa788c0a300c6ead0cc12568ef",
    remote = "https://github.com/dillon-giacoppo/rules_python_external",
    shallow_since = "1582765833 +1100",
)

# Install the rule dependencies
load("@rules_python_external//:repositories.bzl", "rules_python_external_dependencies")

rules_python_external_dependencies()

load("@rules_python_external//:defs.bzl", azure_pip_install = "pip_install")

azure_pip_install(
    name = "azure_py_deps",
    requirements = "//tools/c7n_azure:requirements-bazel-dev.txt",
)

pip3_import(
    name = "azure_py_deps",
    requirements = "//tools/c7n_azure:requirements-bazel-dev.txt",
)

load("@azure_py_deps//:requirements.bzl", "pip_install")

pip_install()

pip3_import(
    name = "gcp_py_deps",
    requirements = "//tools/c7n_gcp:requirements-bazel-dev.txt",
)

load("@gcp_py_deps//:requirements.bzl", "pip_install")

pip_install()

pip3_import(
    name = "mailer_py_deps",
    requirements = "//tools/c7n_mailer:requirements-bazel-dev.txt",
)

load("@mailer_py_deps//:requirements.bzl", "pip_install")

pip_install()

pip3_import(
    name = "kube_py_deps",
    requirements = "//tools/c7n_kube:requirements-bazel-dev.txt",
)

load("@kube_py_deps//:requirements.bzl", "pip_install")

pip_install()

load("@rules_python_external//:defs.bzl", sphinx_pip_install = "pip_install")

sphinx_pip_install(
    name = "sphinx_py_deps",
    requirements = "//tools/c7n_sphinxext:requirements-bazel-dev.txt",
)

setup_versions_repository(
    name = "setup_versions",
    setup_files = [
        "//:setup.py",
        "//tools/c7n_azure:setup.py",
        "//tools/c7n_gcp:setup.py",
        "//tools/c7n_kube:setup.py",
        "//tools/c7n_mailer:setup.py",
    ],
)
