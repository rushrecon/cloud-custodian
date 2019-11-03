load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "c7n_gcp_tests",
    srcs = glob(["**/*.py"]),
    deps = ["@c7n_gcp"],
)

# bazel test --test_env GOOGLE_APPLICATION_CREDENTIALS=external/c7n_gcp_tests/data/credentials.json @c7n_gcp_tests//:test_appengine
py_test(
    name = "test_appengine",
    srcs = ["test_appengine.py"],
    data = ["data/credentials.json"],
    main = "test_appengine.py",
    tags = ["c7n_gcp_test"],
    deps = [":c7n_gcp_tests"],
)

test_suite(
    name = "test_everything",
    tags = ["c7n_gcp_test"],
)
