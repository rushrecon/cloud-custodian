load("@rules_python//python:defs.bzl", "py_binary")

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

# bazel run :c7n_mailer_cli env/mailer-config.yml (? --update-lambda)
py_binary(
    name = "c7n_mailer_cli",
    srcs = ["@c7n_mailer//:cli.py"],
    args = [
        "--run",
    ],
    data = glob(["env/*"]),
    main = "@c7n_mailer//:cli.py",
    deps = [
        "@c7n",
        "@c7n_mailer//:c7n_mailer_cli",
    ],
)

filegroup(
    name = "generated_tests_runner",
    srcs = ["_generated_tests_runner.py"],
    visibility = ["//visibility:public"],
)
