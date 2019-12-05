load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@pip_deps//:requirements.bzl", "requirement")

# TODO: get rid of excluded tests
EXCLUDED_TESTS = [
    # AssertionError: 'azure.vm' not found in 'resources:
    # Not all cloud modules registered
    "test_cli.py",
    #    os.rmdir(path)
    #OSError: [Errno 30] Read-only file system: '/home/pavel/projects/cloud-custodian/tests/data/placebo/test_notify_resource_prep'
    "test_notify.py",
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
    name = "c7n_tests",
    testonly = True,
    srcs = glob(
        ["*.py"],
        EXCLUDED_TESTS,
    ),
    data = glob(["data/**/*"]),
    deps = [
        "//c7n:testing",
        "//tools/c7n_gcp/c7n_gcp:entry",
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
)

[py_test(
    name = test_file[:-3],
    srcs = ["//:generated_tests_runner"],
    args = ["--module=tests." + test_file[:-3]],
    main = "_generated_tests_runner.py",
    tags = ["c7n_test"],
    deps = [":c7n_tests"],
) for test_file in glob(
    ["test_*.py"],
    EXCLUDED_TESTS,
)]

# bazel test :c7n_tests_run
test_suite(
    name = "c7n_tests_run",
    tags = ["c7n_test"],
)
