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

py_library(
    name = "test_deps",
    srcs = ["common.py"],
    data = ["example.jinja"],
    deps = [
        ":azure_mailer",
        ":test_data",
    ],
)

[py_test(
    name = test_file[:-3],
    srcs = [
        "//:generated_tests_runner",
        test_file,
    ],
    args = ["--module=tools.c7n_mailer.tests." + test_file[:-3]],
    imports = ["."],
    main = "_generated_tests_runner.py",
    srcs_version = "PY2AND3",
    deps = [
        ":test_deps",
        "@c7n_mailer//:c7n_mailer_cli",  # used instead of c7n_mailer_core_deps for testing cli as well
    ],
) for test_file in glob(
    ["test_*.py"],
)]

# bazel test //tools/c7n_mailer/tests
test_suite(
    name = "tests",
)
