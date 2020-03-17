load("@rules_python//python:defs.bzl", "py_library")
load("@azure_py_deps//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:private"])

py_library(
    name = "actions",
    visibility = ["//visibility:public"],
    deps = [
        ":base",
        ":delete",
        ":firewall",
        ":lock",
        ":logic_app",
        ":notify",
        ":tagging",
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
    name = "firewall",
    srcs = ["firewall.py"],
    deps = [
        "//c7n:filters",
        # "//tools/c7n_azure/c7n_azure:actions", # avoiding cyclic dependency
        "//tools/c7n_azure/c7n_azure:utils",
        requirement("netaddr"),
    ],
)

py_library(
    name = "lock",
    srcs = ["lock.py"],
    deps = [
        "//c7n:utils",
        # "//tools/c7n_azure/c7n_azure:actions", # avoiding cyclic dependency
        "//tools/c7n_azure/c7n_azure:utils",
        requirement("azure-mgmt-resource"),
    ],
)

py_library(
    name = "logic_app",
    srcs = ["logic_app.py"],
    deps = [
        "//c7n:actions",
        "//c7n:utils",
        requirement("azure-mgmt-logic"),
    ],
)

py_library(
    name = "notify",
    srcs = ["notify.py"],
    deps = [
        "//c7n:actions",
        "//c7n:resolver",
        "//c7n:utils",
        "//tools/c7n_azure/c7n_azure:storage_utils",
        requirement("azure-common"),
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
