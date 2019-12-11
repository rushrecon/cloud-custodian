load("@rules_python//python:defs.bzl", "py_library", "py_test")

package(default_visibility = ["//visibility:private"])

py_library(
    name = "azure_mailer",
    data = glob(["azure_mailer/**/*"]),
    deps = ["@c7n_mailer//:c7n_mailer_azure"],
)

py_library(
    name = "test_data",
    data = glob(["test-templates/*.j2"]),
)

[py_test(
    name = test_file[:-3],
    srcs = [
        "//:generated_tests_runner",
        test_file,
    ],
    args = ["--module=tools.c7n_mailer.tests." + test_file[:-3]],
    main = "_generated_tests_runner.py",
    srcs_version = "PY2AND3",
    deps = [
        ":azure_mailer",
        ":test_data",
        "@c7n_mailer//:c7n_mailer_core_deps",
    ],
) for test_file in glob(
    ["test_*.py"],
)]

# bazel test //tools/c7n_mailer/tests
test_suite(
    name = "tests",
)
