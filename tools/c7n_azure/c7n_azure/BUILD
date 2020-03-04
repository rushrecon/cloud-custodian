load("@rules_python//python:defs.bzl", "py_library")
load("@azure_py_deps//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "azure_lib",
    srcs = glob(["azure/**"]),
)

py_library(
    name = "entry",
    srcs = ["entry.py"],
    imports = ["azure/."],
    deps = [
        ":constants",
        ":storage_utils",
    ],
)

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
    name = "resources",
    srcs = glob(["resources/*"]),
)

py_library(
    name = "storage_utils",
    srcs = ["storage_utils.py"],
    deps = [
        requirement("azure-cosmosdb-table"),
        requirement("azure-cosmos"),
        requirement("azure-common"),
        requirement("azure-mgmt-costmanagement"),
        requirement("azure-mgmt-resourcegraph"),
        requirement("azure-storage-common"),
        requirement("azure-storage-blob"),
        requirement("azure-storage-queue"),
        requirement("azure"),
        requirement("msrest"),
        requirement("msrestazure"),
        requirement("netaddr"),
        ":azure_lib",
        ":constants",
        ":resources",
    ],
)
