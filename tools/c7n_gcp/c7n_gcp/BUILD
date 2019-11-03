package(default_visibility = ["//visibility:public"])

load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@my_deps_gcp//:requirements.bzl", "requirement")

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
