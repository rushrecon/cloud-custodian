load("@rules_python//python:defs.bzl", "py_library")
load("@pip_deps//:requirements.bzl", "requirement")
load("//:c7n_py_test.bzl", "c7n_py_test")

# TODO: get rid of excluded tests
EXCLUDED_TESTS = [
    # 1) AssertionError: 'azure.vm' not found in 'resources:
    # c7n_azure is a stub with no resources available
    # 2) jsonschema.exceptions.SchemaError: {'anyOf': []} is not valid under any of the given schemas
    "test_cli.py",
    # 1) UnboundLocalError: local variable 'invalid' referenced before assignment
    # a blooper
    "test_iamgen.py",
    # 1) AssertionError: False is not true
    # self.assertTrue(content.endswith("hello world"))
    "test_output.py",
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
        "../tools/c7n_gcp/.",
        "../tools/c7n_stub/c7n_azure/.",
        "../tools/c7n_stub/c7n_kube/.",
    ],
    deps = [
        "//c7n:cli",
        "//c7n:commands",
        "//c7n:handler",
        "//c7n:reports",
        "//c7n:sqsexec",
        "//c7n:testing",
        "//c7n:ufuncs",
        "//tools/c7n_gcp/c7n_gcp:entry",
        "//tools/c7n_stub/c7n_azure/c7n_azure:entry",
        "//tools/c7n_stub/c7n_kube/c7n_kube:entry",
        requirement("coverage"),
        requirement("placebo"),
        requirement("flake8"),
        requirement("pytest-xdist"),
        requirement("pytest-cov"),
        requirement("twine"),
        requirement("tox"),
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
    deps = [":c7n_tests_common"],
) for test_file in glob(
    include = ["test_*.py"],
    exclude = EXCLUDED_TESTS,
)]

# bazel test //tests
test_suite(
    name = "tests",
)