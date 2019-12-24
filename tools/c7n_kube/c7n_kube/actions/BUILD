package(default_visibility = ["//visibility:public"])

load("@rules_python//python:defs.bzl", "py_library")
load("@pip_deps//:requirements.bzl", "requirement")

py_library(
    name = "actions_core",
    srcs = [
        "core.py",
    ],
    deps = [
        "//c7n:actions",
        "//c7n:exceptions",
        "//c7n:utils",
    ],
)

py_library(
    name = "actions_labels",
    srcs = [
        "labels.py",
    ],
    deps = [
        ":actions_core",
        "//c7n:utils",
    ],
)

py_library(
    name = "actions_shared",
    srcs = [
        "shared.py",
    ],
    deps = [
        ":actions_core",
        ":actions_labels",
        "//tools/c7n_kube/c7n_kube:provider",
    ],
)
