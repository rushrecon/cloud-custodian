load("@rules_python//python:defs.bzl", "py_library", "py_test")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "c7n_tests",
    srcs = glob(["**/*.py"]),
    deps = ["@c7n"],
)

[py_test(
    name = test_file[:-3],
    srcs = [test_file],
    tags = ["c7n_test"],
    deps = [":c7n_tests"],
) for test_file in glob(["test_*.py"])]

# https://github.com/bazelbuild/bazel/issues/808
# bazel test //tests:c7n_tests_run
test_suite(
    name = "c7n_tests_run",
    tags = ["c7n_test"],
)
