package(default_visibility = ["//visibility:public"])

load("@rules_python//python:defs.bzl", "py_library")
load("@pip_deps//:requirements.bzl", "requirement")

py_library(
    name = "c7n_azure_pip_deps",
    deps = [
        # requirement("azure-mgmt-resource"),
        requirement("vcrpy"),
        requirement("vcrpy_unittest"),
        requirement("backports.functools_lru_cache"),
        # requirement("pywin32"),
        # requirement("sys_platform"),
        requirement("azure-functions"),
        requirement("parameterized"),
    ]
)

py_library(
    name = "entry",
    srcs = ["entry.py"],
    deps = [
        requirement("azure-keyvault"),
        requirement("azure-common"),
        ":provider",
        # ":c7n_azure_pip_deps",
        # ":c7n_azure_rest"
    ]
)

py_library(
    name = "provider",
    srcs = ["provider.py"],
    deps = [
        ":session",
    ]
)

py_library(
    name = "session",
    srcs = ["session.py"],
    deps = [
        # ":c7n_azure_pip_deps",
        # ":c7n_azure_rest"
    ]
)

py_library(
    name = "c7n_azure_rest",
    srcs = [
        "azure_events.py",
        "constants.py",
        "dependency_manager.py",
        "filters.py",
        "function.py",
        "function_package.py",
        "functionapp_utils.py",
        "handler.py",
        "output.py",
        "policy.py",
        "query.py",
        "storage_utils.py",
        "tags.py",
        "utils.py"
    ],
    deps = [
        ":actions",
        ":container_host",
        ":provisioning",
        ":resources"
    ],
)

py_library(
    name = "actions",
    srcs = glob(["actions/*.py"])
)

py_library(
    name = "container_host",
    srcs = glob(["container_host/*.py"])
)

py_library(
    name = "provisioning",
    srcs = glob(["provisioning/*.py"])
)

py_library(
    name = "resources",
    srcs = glob(["resources/*.py"])
)
