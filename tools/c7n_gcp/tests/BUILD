load("@rules_python//python:defs.bzl", "py_library", "py_test")
load("@pip_deps//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:private"])

py_library(
    name = "gcp_common",
    srcs = [
        "gcp_common.py",
        "recorder.py"
    ],
    srcs_version = "PY2AND3",
    deps = [
        "@c7n_gcp",
        # c7n/testing.py
        requirement("mock"),
        requirement("pytest"),
        # c7n/testing.py -> py_test
        requirement("attrs"),
        requirement("importlib_metadata"),
        requirement("more_itertools"),
        requirement("packaging"),
        requirement("pluggy"),
        requirement("py"),
        requirement("zipp"),
        # c7n/testing.py -> c7n/schema.py -> jsonschema
        requirement("pyrsistent"),
    ],
)

[py_test(
    name = test_file[:-3],
    srcs = [test_file],
    data = ["data/credentials.json"],
    srcs_version = "PY2AND3",
    deps = [
        ":gcp_common",
    ],
) for test_file in glob(["test_*.py"])]

test_suite(
    name = "tests",
)
