load("@rules_python//python:defs.bzl", "py_binary")

# bazel run :c7n_aws_cli env/aws-sample.yml
py_binary(
    name = "c7n_aws_cli",
    srcs = ["//c7n:cli.py"],
    args = [
        "run",
        "--cache-period=0",
        "--output-dir=whatever",
    ],
    data = glob(["env/*"]),
    main = "//c7n:cli.py",
    deps = [
        "//c7n",
    ],
)

# bazel run :c7n_gcp_cli env/gcp-sample.yml
py_binary(
    name = "c7n_gcp_cli",
    srcs = ["//c7n:cli.py"],
    args = [
        "run",
        "--cache-period=0",
        "--output-dir=whatever",
    ],
    data = glob(["env/*"]),
    main = "//c7n:cli.py",
    deps = [
        "//c7n",
        "//tools/c7n_gcp/c7n_gcp:entry",
    ],
    imports = [
        "tools/c7n_gcp"
    ],
)

# TODO: consider creating a separate rule for --update-lambda or removing args
# bazel run :c7n_mailer_cli env/mailer-config.yml
py_binary(
    name = "c7n_mailer_cli",
    srcs = ["//tools/c7n_mailer/c7n_mailer:cli.py"],
    args = [
        "--run",
        "-c",
    ],
    data = glob(["env/*"]),
    main = "//tools/c7n_mailer/c7n_mailer:cli.py",
    deps = [
        "//c7n",
        "//tools/c7n_mailer/c7n_mailer:c7n_mailer_cli",
    ],
)