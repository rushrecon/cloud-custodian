package(default_visibility = ["//visibility:public"])

load("@rules_python//python:defs.bzl", "py_library")

py_library(
    name = "common_kube",
    srcs = ["common_kube.py"],
    imports = [".."],
    deps = ["//tools/c7n_stub/c7n_kube/c7n_kube:entry"],
)
