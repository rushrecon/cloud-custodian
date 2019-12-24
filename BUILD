package(default_visibility = ["//visibility:public"])

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

load("//tools/c7n_sphinxext/c7n_sphinxext:foo.bzl", "foo_library")

foo_library(
    name = "ext_files",
    srcs = glob(["docs/**/*"]),
)

foo_library(
    name = "copy_from_tools",
    srcs = [
        "tools/c7n_guardian/readme.md",
        "tools/c7n_logexporter/README.md",
        "tools/c7n_mailer/README.md",
        "tools/c7n_org/README.md",
        "tools/c7n_policystream/README.md",
        "tools/c7n_salactus/README.md",
        "tools/c7n_trailcreator/readme.md",
        "tools/cask/readme.md",
        "tools/omnissm/README.md",
        "tools/omnissm/assets/omnissm.svg",
    ],
)
