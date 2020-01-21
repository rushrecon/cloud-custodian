load("@rules_python//python:defs.bzl", "py_binary")
load("@rules_python//experimental/python:wheel.bzl", "py_package", "py_wheel")

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

# bazel build //:c7n_wheel
py_wheel(
    name = "c7n_wheel",
    console_scripts = {
        "custodian": "c7n.cli:main",
    },
    distribution = "c7n",
    version = "0.8.45.4",
    deps = [
        "//c7n:core_pkg",
    ],
)

# bazel build //:c7n_gcp_wheel
#py_wheel(
#    name = "c7n_gcp_wheel",
#    distribution = "c7n_gcp",
#    version = "0.8.45.4",
#    deps = [
#        "//tools/c7n_gcp/c7n_gcp:gcp_pkg",
#    ],
#)

#sh_binary(
#    name = "c7n_wheel",
#    srcs = ["wheelmaker.sh ."],
#)

#sh_binary(
#    name = "c7n_gcp_wheel",
#    srcs = ["wheelmaker.sh"],
#    args = [
#        "/home/yan/PycharmProjects/cloud-custodian",
#        "tools/c7n_gcp",
#    ],
#)

#sh_binary(
#    name = "c7n_wheel",
#    srcs = ["wheelmaker.sh"],
#    args = [
#        "/home/yan/PycharmProjects/cloud-custodian",
#        ".",
#    ],
#)

#py_wheel(
#    name = "c7n_gcp_wheel",
#    distribution = "c7n",
#    version = "0.0.2",
#    deps = [
#        ":c7n_wheel",
#        "//tools/c7n_gcp/c7n_gcp",
#    ],
#)

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
    imports = [
        "tools/c7n_gcp",
    ],
    main = "//c7n:cli.py",
    deps = [
        "//c7n",
        "//tools/c7n_gcp/c7n_gcp:entry",
    ],
)
