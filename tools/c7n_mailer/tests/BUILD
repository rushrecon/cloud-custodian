load("@rules_python//python:defs.bzl", "py_library")
load("//:c7n_py_test.bzl", "c7n_py_test")

package(default_visibility = ["//visibility:private"])

# TODO: get rid of excluded tests
# All three complaining about azure.xxx imports.
EXCLUDED_AZURE_TESTS = [
    "test_azure.py",
    "test_azure_mailer_utils.py",
    "test_utils.py",
]

py_library(
    name = "azure_mailer",
    data = glob(["azure_mailer/**/*"]),
    imports = [".."],
    deps = ["//tools/c7n_mailer/c7n_mailer:c7n_mailer_azure"],
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

[c7n_py_test(
    name = test_file[:-3],
    srcs = [test_file],
    imports = [
        ".",
        "..",
    ],
    main = test_file,
    srcs_version = "PY2AND3",
    deps = [
        ":test_deps",
        "//tools/c7n_mailer/c7n_mailer:c7n_mailer_cli",  # used instead of c7n_mailer_core_deps for testing cli as well
    ],
) for test_file in glob(
    include = ["test_*.py"],
    exclude = EXCLUDED_AZURE_TESTS,
)]

# bazel test //tools/c7n_mailer/tests
test_suite(
    name = "tests",
)