package(default_visibility = ["//visibility:public"])

load("@rules_python//python:defs.bzl", "py_library")

py_library(
    name = "entry",
    srcs = ["entry.py"],
    deps = [":provider"],
)

py_library(
    name = "provider",
    srcs = ["provider.py"],
    deps = [":resources"],
    #    imports = ["../../../c7n_azure/."],
    #    deps = ["//tools/c7n_azure/c7n_azure:resources"],
)

py_library(
    name = "resource_map",
    srcs = ["resources/resource_map.py"],
)

py_library(
    name = "resources",
    srcs = glob(["resources/*.py"]),
    deps = [":resource_map"],
)
