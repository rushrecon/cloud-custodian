load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "c7n_gcp_tests",
    srcs = glob(["**/*.py"]),
    deps = ["@c7n_gcp"],
)

[py_test(
    name = test_file[:-3],
    srcs = [test_file],
    data = ["data/credentials.json"],
    tags = ["c7n_gcp_test"],
    deps = [":c7n_gcp_tests"],
) for test_file in glob(["test_*.py"])]

## bazel test --test_env=GOOGLE_APPLICATION_CREDENTIALS=external/c7n_gcp_tests/data/credentials.json --test_env=CLOUDSDK_CORE_PROJECT=custodian-1291 --test_output=all @c7n_gcp_tests//:run_all_tests
test_suite(
    name = "run_all_tests",
    tags = ["c7n_gcp_test"],
)
