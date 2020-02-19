load("@rules_python//python:defs.bzl", "py_library")
load("@azure_py_deps//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "c7n_azure_lib",
    srcs = glob(["**/*.py"]),
    deps = [
        ":constants",
        ":storage_utils",
    ],
)

py_library(
    name = "constants",
    srcs = ["constants.py"],
)

py_library(
    name = "storage_utils",
    srcs = ["storage_utils.py"],
    deps = [
        requirement("azure"),
        requirement("azure-common"),
        requirement("azure-storage-common"),
        requirement("azure-storage-blob"),
        requirement("azure-storage-queue"),
        requirement("msrest"),
        requirement("msrestazure"),
        requirement("netaddr"),
        ":constants",
    ],
)
