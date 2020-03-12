load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "resources",
    srcs = glob(["*.py"]),
    deps = [
        "//tools/c7n_azure/c7n_azure:filters",
        "//tools/c7n_azure/c7n_azure:query",
        "//tools/c7n_azure/c7n_azure/actions",
    ],
)
