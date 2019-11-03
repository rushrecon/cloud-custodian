load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "c7n_gcp_tests",
    srcs = glob(["**/*.py"]),
    deps = ["@c7n_gcp"],
)

py_test(
    name = "test_appengine",
    srcs = ["test_appengine.py"],
    main = "test_appengine.py",
    deps = [":c7n_gcp_tests"],
)
