# https://github.com/bazelbuild/rules_python
load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@my_deps//:requirements.bzl", "pip_install")

#pip_install()
#
#load("@my_deps//:requirements.bzl", "requirement")

py_library(
    name = "custodian-test",
    srcs = ["c7n/version.py"],
    #    deps = [requirement("pytest")],
)

py_binary(
    name = "custodian-test-bin",
    srcs = ["c7n/version-main.py"],
    main = "c7n/version-main.py",
    deps = [":custodian-test"],
)
