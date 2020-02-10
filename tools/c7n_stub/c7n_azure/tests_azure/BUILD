package(default_visibility = ["//visibility:public"])

load("@rules_python//python:defs.bzl", "py_library")

py_library(
    name = "azure_common",
    srcs = ["azure_common.py"],
    imports = [".."],
    deps = ["//tools/c7n_stub/c7n_azure/c7n_azure:entry"],
)
