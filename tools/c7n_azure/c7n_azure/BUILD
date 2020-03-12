load("@rules_python//python:defs.bzl", "py_library")
load("@azure_py_deps//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "azure_lib",
    deps = [
        ":function",
    ],
)

py_library(
    name = "actions",
    deps = ["//tools/c7n_azure/c7n_azure/actions"],
)

py_library(
    name = "container_host",
    deps = ["//tools/c7n_azure/c7n_azure/container_host"],
)

py_library(
    name = "provisioning",
    deps = ["//tools/c7n_azure/c7n_azure/provisioning"],
)

py_library(
    name = "resources",
    deps = ["//tools/c7n_azure/c7n_azure/resources"],
)

py_library(
    name = "azure_events",
    srcs = ["azure_events.py"],
    deps = [
        ":session",
    ],
)

py_library(
    name = "constants",
    srcs = ["constants.py"],
)

py_library(
    name = "dependency_manager",
    srcs = ["dependency_manager.py"],
    deps = [
        ":constants",
        ":provisioning",
        ":session",
        ":storage_utils",
        ":utils",
    ],
)

py_library(
    name = "entry",
    srcs = ["entry.py"],
    deps = [
        ":container_host",
        ":output",
        ":policy",
        ":provider",
    ],
)

py_library(
    name = "filters",
    srcs = ["filters.py"],
    deps = [
        ":tags",
        ":utils",
    ],
)

py_library(
    name = "function",
    srcs = ["function.py"],
    deps = [
        ":entry",
        ":handler",
        ":utils",
    ],
)

py_library(
    name = "function_package",
    srcs = ["function_package.py"],
    deps = [
        ":constants",
        ":dependency_manager",
        ":session",
    ],
)

py_library(
    name = "functionapp_utils",
    srcs = ["functionapp_utils.py"],
    deps = [
        ":constants",
        ":provisioning",
        ":session",
        ":storage_utils",
        ":utils",
    ],
)

py_library(
    name = "handler",
    srcs = ["handler.py"],
    deps = [
        ":provider",
    ],
)

py_library(
    name = "output",
    srcs = ["output.py"],
    deps = [
        ":storage_utils",
        ":utils",
    ],
)

py_library(
    name = "policy",
    srcs = ["policy.py"],
    deps = [
        ":azure_events",
        ":constants",
        ":function_package",
        ":functionapp_utils",
        ":resources",
        ":storage_utils",
        ":utils",
    ],
)

py_library(
    name = "provider",
    srcs = ["provider.py"],
    deps = [
        ":resources",
    ],
)

py_library(
    name = "query",
    srcs = ["query.py"],
    deps = [
        ":actions",
        ":constants",
        ":filters",
        ":provider",
    ],
)

py_library(
    name = "session",
    srcs = ["session.py"],
    deps = [
        ":constants",
        #        ":utils", # avoiding cyclic dependency
    ],
)

py_library(
    name = "storage_utils",
    srcs = ["storage_utils.py"],
    deps = [
        ":constants",
    ],
)

py_library(
    name = "tags",
    srcs = ["tags.py"],
    deps = [
        ":utils",
    ],
)

py_library(
    name = "utils",
    srcs = ["utils.py"],
    deps = [
        ":constants",
        ":session",
    ],
)
