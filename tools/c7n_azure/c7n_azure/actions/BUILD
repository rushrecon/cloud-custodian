load("@rules_python//python:defs.bzl", "py_library")
load("@azure_py_deps//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "actions",
    srcs = glob(
        include = ["*.py"],
        exclude = [
            "base.py",
            "delete.py",
        ],
    ),
    deps = [
        ":base",
        ":delete",
        "//tools/c7n_azure/c7n_azure:tags",
    ],
)

py_library(
    name = "base",
    srcs = ["base.py"],
    deps = [
        "//c7n:actions",
        "//tools/c7n_azure/c7n_azure:constants",
        "//tools/c7n_azure/c7n_azure:utils",
        requirement("msrestazure"),
    ],
)

py_library(
    name = "delete",
    srcs = ["delete.py"],
    deps = [
        "//c7n:utils",
        "//tools/c7n_azure/c7n_azure:actions",
        "//tools/c7n_azure/c7n_azure:utils",
    ],
)
