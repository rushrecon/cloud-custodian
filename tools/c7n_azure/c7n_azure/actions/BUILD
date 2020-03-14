load("@rules_python//python:defs.bzl", "py_library")
load("@azure_py_deps//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:private"])

py_library(
    name = "actions",
    srcs = glob(
        include = ["*.py"],
        exclude = [
            "base.py",
            "delete.py",
            "tagging.py",
        ],
    ),
    visibility = ["//visibility:public"],
    deps = [
        ":base",
        ":delete",
        ":tagging",
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
        # "//tools/c7n_azure/c7n_azure:actions", # avoiding cyclic dependency
        "//tools/c7n_azure/c7n_azure:utils",
    ],
)

py_library(
    name = "tagging",
    srcs = ["tagging.py"],
    deps = [
        requirement("jmespath"),
        "//tools/c7n_azure/c7n_azure:constants",
        "//tools/c7n_azure/c7n_azure:tags",
        "//tools/c7n_azure/c7n_azure:utils",
        requirement("python-dateutil"),
        requirement("msrest"),
        "//c7n:exceptions",
        "//c7n:filters",
        "//c7n:lookup",
        "//c7n:utils",
    ],
)
