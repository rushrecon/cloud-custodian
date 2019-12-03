load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@pip_deps//:requirements.bzl", "requirement")

# bazel run :c7n_aws_cli env/aws-sample.yml
py_binary(
    name = "c7n_aws_cli",
    srcs = ["@c7n//:cli.py"],
    args = [
        "run",
        "--cache-period=0",
        "--output-dir=whatever",
    ],
    data = glob(["env/*"]),
    main = "@c7n//:cli.py",
    deps = [
        "@c7n",
    ],
)

# bazel run :c7n_gcp_cli env/gcp-sample.yml
py_binary(
    name = "c7n_gcp_cli",
    srcs = ["@c7n//:cli.py"],
    args = [
        "run",
        "--cache-period=0",
        "--output-dir=whatever",
    ],
    data = glob(["env/*"]),
    main = "@c7n//:cli.py",
    deps = [
        "@c7n",
        "@c7n_gcp//:entry",
    ],
)

# TODO: get rid of excluded tests
EXCLUDED_TESTS = [
    # AssertionError: 'azure.vm' not found in 'resources:
    # Not all cloud modules registered
    "tests/test_cli.py",
    #    os.rmdir(path)
    #OSError: [Errno 30] Read-only file system: '/home/pavel/projects/cloud-custodian/tests/data/placebo/test_notify_resource_prep'
    "tests/test_notify.py",
    # self.assertTrue(content.endswith("hello world"))
    # AssertionError: False is not true
    "tests/test_output.py",
    # First extra element 2:
    #- ['aws', 'gcp']
    #+ ['aws', 'azure', 'gcp', 'k8s']
    # Not all cloud modules registered
    "tests/test_provider.py",
    # ERROR: test_json_diff_pitr (tests.test_revisions.SGDiffLibTest)
    #c7n.exceptions.PolicyValidationError: securitygroup.filters Invalid filter type {'type': 'json-diff', 'selector': 'date', 'selector_value': '2016/12/11 17:25Z'}
    "tests/test_revisions.py",
]

# TODO: find a way to move section below into /tests package, relative import is major blocker now
py_library(
    name = "c7n_tests",
    testonly = True,
    srcs = glob(
        ["tests/*.py"],
        EXCLUDED_TESTS,
    ),
    data = glob(["tests/data/**/*"]),
    srcs_version = "PY2AND3",
    deps = [
        "@c7n//:testing",
        "@c7n_gcp//:entry",
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
    name = test_file[:-3].replace("tests/", ""),
    srcs = ["_generated_tests_runner.py"],
    args = ["--module=" + test_file[:-3].replace("/", ".")],
    main = "_generated_tests_runner.py",
    tags = ["c7n_test"],
    deps = [":c7n_tests"],
) for test_file in glob(
    ["tests/test_*.py"],
    EXCLUDED_TESTS,
)]

# bazel test :c7n_tests_run
test_suite(
    name = "c7n_tests_run",
    tags = ["c7n_test"],
)
