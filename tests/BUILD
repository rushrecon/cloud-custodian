load("@rules_python//python:defs.bzl", "py_library", "py_test")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "c7n_tests",
    srcs = glob(["**/*.py"]),
    deps = ["@c7n"],
)
