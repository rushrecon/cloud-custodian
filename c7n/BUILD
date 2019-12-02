package(default_visibility = ["//visibility:public"])

load("@rules_python//python:defs.bzl", "py_library")
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
    name = "resources",
    srcs = glob(["resources/*.py"]),
    deps = [
        ":actions",
        ":credentials",
        ":log",
        ":query",
        requirement("botocore"),
        requirement("boto3"),
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
    srcs = [
        "testing.py",
    ],
    testonly = True,
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
