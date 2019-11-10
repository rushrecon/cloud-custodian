load("@rules_python//python:defs.bzl", "py_library", "py_test")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "c7n_gcp_tests",
    srcs = glob(["**/*.py"]),
    srcs_version = "PY2AND3",
    deps = ["@c7n_gcp"],
)

[py_test(
    name = test_file[:-3],
    srcs = [test_file],
    data = ["data/credentials.json"],
    srcs_version = "PY2AND3",
    tags = ["c7n_gcp_test"],
    deps = [":c7n_gcp_tests"],
) for test_file in glob(["test_*.py"])]

# bazel test //tools/c7n_gcp/tests:c7n_gcp_tests_run
test_suite(
    name = "c7n_gcp_tests_run",
    tags = ["c7n_gcp_test"],
)
