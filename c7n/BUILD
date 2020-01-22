package(default_visibility = ["//visibility:public"])

CORE_PIP_DEPS_REP = "core_pip_deps"

load("@rules_python//python:defs.bzl", "py_library")
load("@core_pip_deps//:requirements.bzl", "all_requirements", "requirement")
load("@rules_python//experimental/python:wheel.bzl", "py_package")

#c7n_core_requirements = [requirement(i) for i in c7n_core_requirements]

c7n_core_requirements = [i for i in all_requirements]

c7n_core_requirements = c7n_core_requirements

py_library(
    name = "c7n_core_lib",
    #    srcs = c7n_core_requirements,
    deps = c7n_core_requirements,
)

py_package(
    name = "core_pkg",
    # Only include these Python packages.
    deps = [
        "c7n",
        ":c7n_core_lib",
    ],
)

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

py_library(
    name = "cli",
    srcs = [
        "cli.py",
    ],
    deps = [
        ":commands",
        ":config",
        requirement("argcomplete"),
    ],
)

py_library(
    name = "commands",
    srcs = [
        "commands.py",
    ],
    deps = [
        ":config",
        ":exceptions",
        ":policy",
        ":provider",
        ":resources",
        ":schema",
        ":utils",
        requirement("six"),
        requirement("PyYAML"),
    ],
)

py_library(
    name = "sqsexec",
    srcs = [
        "sqsexec.py",
    ],
    deps = [
        ":utils",
    ],
)

py_library(
    name = "exceptions",
    srcs = [
        "exceptions.py",
    ],
)

py_library(
    name = "actions",
    srcs = glob(["actions/*.py"]),
)

py_library(
    name = "ufuncs",
    srcs = glob(["ufuncs/*.py"]),
)

py_library(
    name = "reports",
    srcs = glob(["reports/*.py"]),
)

py_library(
    name = "handler",
    srcs = [
        "handler.py",
    ],
    deps = [
        ":config",
        ":policy",
        ":resources",
        ":utils",
        requirement("boto3"),
    ],
)

py_library(
    name = "resources",
    srcs = glob(["resources/*.py"]),
    deps = [
        ":actions",
        ":credentials",
        ":log",
        ":query",
        requirement("botocore"),
        requirement("boto3"),
        requirement("aws_xray_sdk"),
        # transitive: aws_xray_sdk
        requirement("jsonpickle"),
    ],
)

py_library(
    name = "log",
    srcs = ["log.py"],
)

py_library(
    name = "tags",
    srcs = ["tags.py"],
)

py_library(
    name = "credentials",
    srcs = ["credentials.py"],
)

py_library(
    name = "query",
    srcs = ["query.py"],
    deps = [
        ":tags",
    ],
)

py_library(
    name = "filters",
    srcs = glob(["filters/*.py"]),
    deps = [
        ":executor",
        ":manager",
        # transitive: revisions.py
        requirement("jsonpatch"),
    ],
)

py_library(
    name = "manager",
    srcs = [
        "manager.py",
    ],
    deps = [
        ":cache",
    ],
)

py_library(
    name = "cache",
    srcs = [
        "cache.py",
    ],
)

py_library(
    name = "utils",
    srcs = [
        "utils.py",
    ],
    deps = [
        ":config",
        ":ipaddress",
    ],
)

py_library(
    name = "registry",
    srcs = [
        "registry.py",
    ],
)

py_library(
    name = "ipaddress",
    srcs = [
        "ipaddress.py",
    ],
)

py_library(
    name = "config",
    srcs = [
        "config.py",
    ],
)

py_library(
    name = "output",
    srcs = [
        "output.py",
    ],
    deps = [
        ":exceptions",
        ":registry",
        ":utils",
    ],
)

py_library(
    name = "version",
    srcs = [
        "version.py",
    ],
)

py_library(
    name = "ctx",
    srcs = [
        "ctx.py",
    ],
    deps = [
        ":output",
        ":utils",
        ":version",
    ],
)

py_library(
    name = "cwe",
    srcs = [
        "cwe.py",
    ],
    deps = [
        ":ctx",
    ],
)

py_library(
    name = "provider",
    srcs = [
        "provider.py",
    ],
)

py_library(
    name = "policy",
    srcs = [
        "policy.py",
    ],
    deps = [
        ":cwe",
        ":provider",
        ":resources",
        requirement("python-dateutil"),
    ],
)

py_library(
    name = "logs_support",
    srcs = [
        "logs_support.py",
    ],
)

py_library(
    name = "mu",
    srcs = [
        "mu.py",
    ],
    deps = [
        ":logs_support",
    ],
)

py_library(
    name = "executor",
    srcs = [
        "executor.py",
    ],
)

py_library(
    name = "lookup",
    srcs = [
        "lookup.py",
    ],
)

py_library(
    name = "schema",
    srcs = [
        "schema.py",
    ],
    deps = [
        ":filters",
        ":resolver",
        ":structure",
        requirement("jsonschema"),
        # transitive: jsonschema
        requirement("pyrsistent"),
    ],
)

py_library(
    name = "resolver",
    srcs = [
        "resolver.py",
    ],
)

py_library(
    name = "structure",
    srcs = [
        "structure.py",
    ],
)

py_library(
    name = "testing",
    testonly = True,
    srcs = [
        "testing.py",
    ],
    deps = [
        ":policy",
        ":schema",
        requirement("mock"),
        requirement("pytest"),
        requirement("jmespath"),
        requirement("pyyaml"),
        # transitive: py_test
        requirement("packaging"),
        requirement("pluggy"),
        requirement("py"),
        requirement("attrs"),
        requirement("more_itertools"),
        requirement("importlib_metadata"),
        requirement("zipp"),
        requirement("uritemplate"),
    ],
)
