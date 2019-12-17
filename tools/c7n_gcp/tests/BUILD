load("@rules_python//python:defs.bzl", "py_library")
load("//:c7n_py_test.bzl", "c7n_py_test")

package(default_visibility = ["//visibility:private"])

py_library(
    name = "gcp_common",
    testonly = True,
    srcs = [
        "gcp_common.py",
        "recorder.py",
    ],
    imports = [".."],
    srcs_version = "PY2AND3",
    deps = [
        "//c7n:testing",
        "//tools/c7n_gcp/c7n_gcp:client",
        "//tools/c7n_gcp/c7n_gcp:handler",  # for test_mu_gcp.py only
    ],
)

[c7n_py_test(
    name = test_file[:-3],
    srcs = [test_file],
    data = glob(["data/**"]),
    srcs_version = "PY2AND3",
    imports = ["."],
    deps = [":gcp_common"],
) for test_file in glob(["test_*.py"])]

# bazel test //tools/c7n_gcp/tests
test_suite(
    name = "tests",
)
