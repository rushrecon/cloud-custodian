load("@rules_python//python:defs.bzl", "py_library")
load("@pip_deps//:requirements.bzl", "requirement")
load("//:c7n_py_test.bzl", "c7n_py_test")

# TODO: get rid of excluded tests
EXCLUDED_TESTS = [
    # AssertionError: 'azure.vm' not found in 'resources:
    # Not all cloud modules registered
    "test_cli.py",
    # self.assertTrue(content.endswith("hello world"))
    # AssertionError: False is not true
    "test_output.py",
    # First extra element 2:
    #- ['aws', 'gcp']
    #+ ['aws', 'azure', 'gcp', 'k8s']
    # Not all cloud modules registered
    "test_provider.py",
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
    deps = [
        "//c7n:cli",
        "//c7n:commands",
        "//c7n:handler",
        "//c7n:reports",
        "//c7n:sqsexec",
        "//c7n:testing",
        "//c7n:ufuncs",
        #        "//tools/c7n_gcp/c7n_gcp:entry",
        requirement("coverage"),
        requirement("placebo"),
        requirement("flake8"),
        requirement("pytest-xdist"),
        requirement("pytest-cov"),
        requirement("twine"),
        requirement("tox"),
        requirement("six"),
        requirement("psutil"),
        requirement("fakeredis"),
        requirement("tabulate"),
        requirement("argcomplete"),
        requirement("vcrpy"),
        requirement("wrapt"),
    ],
    #    imports = ["../tools/c7n_gcp/."],
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
