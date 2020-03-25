load("@rules_python//python:defs.bzl", "py_library")
load("@pip_deps//:requirements.bzl", "requirement")
load("//:c7n_py_test.bzl", "c7n_py_test")
load("//:builddefs.bzl", "EXCLUDED_PKGS")

package(default_visibility = ["//visibility:private"])

# TODO: get rid of excluded tests; remember to update bazel-test-excluded.yml
EXCLUDED_TESTS = [
    # 1) jsonschema.exceptions.SchemaError: {'anyOf': []} is not valid under any of the given schemas

    # If we run Test 1 from test_log first it throws an unexpected exception.
    # However if another  self.run_and_expect_failure runs before Test 1 from test_log it runs correctly.
    # E.g. you can uncomment the line bellow
    # self.run_and_expect_failure(["custodian", "schema", "ec2.filters.and.foo"], 1)
    "test_cli.py",
]

py_library(
    name = "c7n_tests_common",
    testonly = True,
    srcs = glob([
        "common.py",
        "zpill.py",
        "test_offhours.py",
        "test_s3.py",
    ]),
    data = glob(["data/**/*"]) + [":placebo_data.zip"],
    imports = [
        "../tools/c7n_azure/.",
        "../tools/c7n_gcp/.",
        "../tools/c7n_kube/.",
    ],
    deps = [
        "//c7n:cli",
        "//c7n:commands",
        "//c7n:handler",
        "//c7n:reports",
        "//c7n:sqsexec",
        "//c7n:testing",
        "//c7n:ufuncs",
        "//tools/c7n_azure/c7n_azure:entry",
        "//tools/c7n_gcp/c7n_gcp:entry",
        "//tools/c7n_kube/c7n_kube:entry",
        requirement("coverage"),
        requirement("placebo"),
        requirement("flake8"),
        requirement("pytest-xdist"),
        requirement("pytest-cov"),
        requirement("twine"),
        requirement("tox"),
        requirement("toml"),
        requirement("six"),
        requirement("psutil"),
        requirement("jsonpointer"),
        requirement("fakeredis"),
        requirement("tabulate"),
        requirement("argcomplete"),
        requirement("vcrpy"),
        requirement("wrapt"),
    ],
)

[c7n_py_test(
    name = test_file[:-3],
    srcs = [test_file],
    excluded_pkgs = EXCLUDED_PKGS,
    tags = ["first_chunk" if test_file[:-3] < "test_kafka" else "second_chunk"],
    deps = [":c7n_tests_common"],
) for test_file in glob(
    include = ["test_*.py"],
    exclude = EXCLUDED_TESTS,
)]

# bazel test //tests
test_suite(
    name = "tests",
    tests = [
        "first_chunk",
        "second_chunk",
    ],
)

# bazel test //tests:first_chunk
test_suite(
    name = "first_chunk",
    tags = ["first_chunk"],
)

# bazel test //tests:second_chunk
test_suite(
    name = "second_chunk",
    tags = ["second_chunk"],
)
