load("@rules_python//python:defs.bzl", "py_library")
load("@kube_py_deps//:requirements.bzl", "all_requirements", "requirement")
load("//:c7n_py_test.bzl", "c7n_py_test")

EXCLUDED_PKGS = [
    "azure_cosmosdb_nspkg",
]
package(default_visibility = ["//visibility:private"])

pip_deps = [i for i in all_requirements]

[print(i) for i in all_requirements]

py_library(
    name = "azure_lib",
    srcs = glob(["azure/**"]),
)

py_library(
    name = "kube_common_deps",
    testonly = True,
    deps = [
        "//tools/c7n_kube/c7n_kube:entry",
        "//tools/c7n_kube/c7n_kube:filters",
        "//tools/c7n_kube/c7n_kube:provider",
        "//tools/c7n_kube/c7n_kube:query",
    ],
)

py_library(
    name = "kube_common",
    testonly = True,
    srcs = [
        "common_kube.py",
    ],
    imports = [
        "..",
        "../../c7n_azure/.",
        "../../c7n_azure/c7n_azure/azure",
        "../../c7n_azure/c7n_gcp/.",
        "../../c7n_gcp/.",
    ],
    srcs_version = "PY2AND3",
    deps = [
        ":kube_common_deps",
        "//c7n:testing",
        "//tools/c7n_azure/c7n_azure:c7n_azure_lib",
        "//tools/c7n_azure/c7n_azure:entry",
        "//tools/c7n_azure/c7n_azure:storage_utils",
        "//tools/c7n_gcp/c7n_gcp:entry",
    ],
)

[c7n_py_test(
    name = test_file[:-3],
    srcs = [test_file],
    data = glob(["data/**"]),
    imports = ["."],
    legacy_create_init = 0,
    srcs_version = "PY2AND3",
    excluded_pkgs = EXCLUDED_PKGS,
    deps = [
        ":kube_common",
        ":azure_lib",
        #        requirement("azure-cosmosdb-table"),
    ] + pip_deps,
) for test_file in glob(["test_*.py"])]

# bazel test //tools/c7n_kube/tests
test_suite(
    name = "tests",
)
