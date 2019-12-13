load("@rules_python//python:defs.bzl", "py_library", "py_test")

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

py_library(
    name = "test_data",
    data = glob(["data/**"]),
)

[py_test(
    name = test_file[:-3],
    srcs = [
        "//:generated_tests_runner",
        test_file,
    ],
    args = ["--module=tools.c7n_gcp.tests." + test_file[:-3]],
    main = "_generated_tests_runner.py",
    deps = [
        ":gcp_common",
        ":test_data",
    ],
) for test_file in glob(["test_*.py"])]

# bazel test //tools/c7n_gcp/tests
test_suite(
    name = "tests",
)
