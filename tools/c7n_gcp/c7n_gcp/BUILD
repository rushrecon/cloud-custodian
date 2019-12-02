package(default_visibility = ["//visibility:public"])

load("@rules_python//python:defs.bzl", "py_library")
load("@pip_deps//:requirements.bzl", "requirement")

py_library(
    name = "c7n_gcp",
    srcs = glob(["**/*.py"]),
    deps = [
        "@c7n",
        # Solve build failures:
        requirement("cachetools"),
        requirement("pyasn1"),
        requirement("pyasn1_modules"),
        requirement("rsa"),
        # Originals:
        requirement("retrying"),
        requirement("google-api-python-client"),
        requirement("ratelimiter"),
        requirement("google-auth"),
        requirement("google-auth-httplib2"),
        requirement("google-cloud-logging"),
        requirement("google-cloud-monitoring"),
    ],
)

py_library(
    name = "provider",
    srcs = ["provider.py"],
    deps = [
        ":client",
        "@c7n//:provider",
        "@c7n//:registry",
    ],
)

py_library(
    name = "handler",
    srcs = [
        "handler.py",
    ],
    deps = [
        ":entry",
    ],
)

py_library(
    name = "query",
    srcs = [
        "query.py",
    ],
)

py_library(
    name = "resources",
    srcs = glob(["resources/*.py"]),
    deps = [
        ":query",
    ],
)

py_library(
    name = "filters",
    srcs = glob(["filters/*.py"]),
)

py_library(
    name = "actions",
    srcs = glob(["actions/*.py"]),
    deps = [
        ":filters",
        ":provider",
        "@c7n//:lookup",
    ],
)

py_library(
    name = "output",
    srcs = ["output.py"],
    deps = [
        "@c7n//:output",
    ],
)

py_library(
    name = "mu",
    srcs = ["mu.py"],
    deps = [
        "@c7n//:mu",
    ],
)

py_library(
    name = "policy",
    srcs = ["policy.py"],
    deps = [
        ":mu",
    ],
)

py_library(
    name = "entry",
    srcs = ["entry.py"],
    deps = [
        ":actions",
        ":output",
        ":policy",
        ":resources",
        "@c7n//:lookup",
    ],
)

py_library(
    name = "client",
    srcs = ["client.py"],
    deps = [
        requirement("cachetools"),
        requirement("pyasn1"),
        requirement("pyasn1_modules"),
        requirement("rsa"),
        requirement("retrying"),
        requirement("google-api-python-client"),
        requirement("ratelimiter"),
        requirement("google-auth"),
        requirement("google-auth-httplib2"),
        requirement("google-cloud-logging"),
        requirement("google-cloud-monitoring"),
    ],
)
