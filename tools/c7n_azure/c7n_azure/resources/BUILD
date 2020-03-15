load("@rules_python//python:defs.bzl", "py_library")
load("@azure_py_deps//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:private"])

py_library(
    name = "resources",
    srcs = glob(["*.py"]),
    visibility = ["//visibility:public"],
    deps = [
        "//tools/c7n_azure/c7n_azure:filters",
        "//tools/c7n_azure/c7n_azure:query",
        "//tools/c7n_azure/c7n_azure/actions",
        requirement("azure-cosmosdb-table"),
        requirement("azure-cosmos"),
        requirement("azure-common"),
    ],
)
