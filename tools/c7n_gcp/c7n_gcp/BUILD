package(default_visibility = ["//visibility:public"])

load("@rules_python//python:defs.bzl", "py_library")
load("@gcp_pip_deps//:requirements.bzl", "all_requirements", "requirement")
load("@rules_python//experimental/python:wheel.bzl", "py_package")

#c7n_core_requirements = [requirement(i) for i in c7n_core_requirements]

c7n_gcp_requirements = [i for i in all_requirements]

c7n_gcp_requirements = c7n_gcp_requirements

py_library(
    name = "c7n_gcp_lib",
    srcs = ["entry.py"],
    deps = c7n_gcp_requirements,
)

py_package(
    name = "gcp_pkg",
    # Only include these Python packages.
    deps = [
        ":c7n_gcp_lib",
    ],
)

#py_library(
#    name = "c7n_gcp",
#    srcs = glob(["**/*.py"]),
#    deps = [
#        requirement("argcomplete"),
#        requirement("boto3"),
#        requirement("botocore"),
#        requirement("jsonschema"),
#        requirement("PyYAML"),
#        requirement("tabulate"),
#        requirement("jsonpatch"),
#        requirement("futures"),
#        requirement("python-dateutil"),
#        requirement("urllib3"),
#        requirement("certifi"),
#    ],
#)
#
#py_library(
#    name = "actions",
#    srcs = glob(["actions/*.py"]),
#    deps = [
#        ":filters",
#        ":provider",
#        "//c7n:actions",
#        "//c7n:filters",
#        "//c7n:lookup",
#        "//c7n:resolver",
#        "//c7n:utils",
#    ],
#)
#
#py_library(
#    name = "filters",
#    srcs = glob(["filters/*.py"]),
#    deps = [
#        "//c7n:filters",
#        "//c7n:utils",
#    ],
#)
#
#py_library(
#    name = "resources",
#    srcs = glob(["resources/*.py"]),
#    deps = [
#        ":actions",
#        ":provider",
#        ":query",
#        "//c7n:filters",
#        "//c7n:utils",
#        requirement("jmespath"),
#    ],
#)
#
#py_library(
#    name = "client",
#    srcs = ["client.py"],
#    deps = [
#        requirement("cachetools"),
#        requirement("pyasn1"),
#        requirement("pyasn1_modules"),
#        requirement("rsa"),
#        requirement("retrying"),
#        requirement("google-api-python-client"),
#        requirement("ratelimiter"),
#        requirement("google-auth"),
#        requirement("google-auth-httplib2"),
#        requirement("google-cloud-logging"),
#        requirement("google-cloud-monitoring"),
#        requirement("six"),
#    ],
#)
#
#py_library(
#    name = "entry",
#    srcs = ["entry.py"],
#    deps = [
#        ":actions",
#        ":filters",
#        ":output",
#        ":policy",
#        ":provider",
#        ":resources",
#    ],
#)
#
#py_library(
#    name = "handler",
#    srcs = [
#        "handler.py",
#    ],
#    deps = [
#        ":entry",
#        "//c7n:config",
#        "//c7n:policy",
#    ],
#)
#
#py_library(
#    name = "mu",
#    srcs = ["mu.py"],
#    deps = [
#        ":client",
#        "//c7n:mu",
#        "//c7n:utils",
#        requirement("google-api-python-client"),
#    ],
#)
#
#py_library(
#    name = "output",
#    srcs = ["output.py"],
#    deps = [
#        "//c7n:output",
#        "//c7n:utils",
#        requirement("google-cloud-logging"),
#    ],
#)
#
#py_library(
#    name = "policy",
#    srcs = ["policy.py"],
#    deps = [
#        ":mu",
#        "//c7n:exceptions",
#        "//c7n:policy",
#        "//c7n:utils",
#    ],
#)
#
#py_library(
#    name = "provider",
#    srcs = ["provider.py"],
#    deps = [
#        ":client",
#        "//c7n:provider",
#        "//c7n:registry",
#    ],
#)
#
#py_library(
#    name = "query",
#    srcs = ["query.py"],
#    deps = [
#        "//c7n:actions",
#        "//c7n:filters",
#        "//c7n:manager",
#        "//c7n:query",
#        "//c7n:utils",
#        requirement("google-api-python-client"),
#        requirement("six"),
#        requirement("jmespath"),
#    ],
#)
