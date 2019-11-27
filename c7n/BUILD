package(default_visibility = ["//visibility:public"])

load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@pip_deps//:requirements.bzl", "requirement")

py_library(
    name = "c7n",
    srcs = glob(["**/*.py"]),
    deps = [
        requirement("argcomplete"),
        requirement("boto3"),
        requirement("botocore"),
        requirement("jsonschema"),
        requirement("PyYAML"),
        requirement("tabulate"),
        requirement("jsonpatch"),
        requirement("futures"),
        requirement("python-dateutil"),
        requirement("urllib3"),
        requirement("certifi"),
    ],
)
