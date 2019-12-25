load("@rules_python//python:defs.bzl", "py_library")
load("//:c7n_py_test.bzl", "c7n_py_test")

package(default_visibility = ["//visibility:private"])

py_library(
    name = "kube_common_deps",
    testonly = True,
    deps = [
        "//tools/c7n_kube/c7n_kube:entry",
        "//tools/c7n_kube/c7n_kube:filters",
        "//tools/c7n_kube/c7n_kube:provider",
        "//tools/c7n_kube/c7n_kube:query",
    ],
)

py_library(
    name = "kube_common",
    testonly = True,
    srcs = [
        "common_kube.py",
    ],
    imports = [".."],
    srcs_version = "PY2AND3",
    deps = [
        ":kube_common_deps",
        "//c7n:testing",
    ],
)

[c7n_py_test(
    name = test_file[:-3],
    srcs = [test_file],
    data = glob(["data/**"]),
    imports = ["."],
    srcs_version = "PY2AND3",
    deps = [":kube_common"],
) for test_file in glob(["test_*.py"])]

# bazel test //tools/c7n_kube/tests
test_suite(
    name = "tests",
)
