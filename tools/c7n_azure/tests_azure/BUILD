load("@rules_python//python:defs.bzl", "py_library")
load("//:c7n_py_test.bzl", "c7n_py_test")
load("@azure_py_deps//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:private"])

py_library(
    name = "azure_common",
    testonly = True,
    srcs = [
        "azure_common.py",
    ],
    imports = [".."],
    srcs_version = "PY2AND3",
    deps = [
        ":azure_serializer",
        ":tools_tags",
        "//c7n:testing",
        #        "//tools/c7n_azure/c7n_azure:constants",
        "//tools/c7n_azure/c7n_azure:azure_lib",
    ],
)

py_library(
    name = "azure_serializer",
    testonly = True,
    srcs = ["azure_serializer.py"],
)

py_library(
    name = "tools_tags",
    srcs = ["tools_tags.py"],
    deps = [requirement("azure-mgmt-resourcegraph")],
)

[c7n_py_test(
    name = test_file[:-3],
    srcs = [test_file],
    data = glob(["data/**"]),
    imports = ["."],
    srcs_version = "PY2AND3",
    deps = [":azure_common"],
) for test_file in glob(["test_*.py"])]

# bazel test //tools/c7n_azure/tests_azure:tests
test_suite(
    name = "tests",
)
