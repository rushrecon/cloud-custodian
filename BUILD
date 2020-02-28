load("@rules_python//python:defs.bzl", "py_binary")
load("//:py_wheel_extension.bzl", "py_wheel_entry_points_ext")
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

sh_binary(
    name = "run-add-ep-script",
    srcs = ["add-entry-points-to-wheel.sh"],
    data = ["file_hash.py"],
)

# bazel build //:c7n_wheel
# To install a generated whl-file into your env: pip install <WORKSPACE_directory>/bazel-bin/<file_name>.whl
py_wheel(
    name = "c7n_wheel",
    console_scripts = {
        "custodian": "c7n.cli:main",
    },
    distribution = "c7n",
    # the version is from setup.py
    version = "0.8.45.4",
    deps = [
        "//c7n:core_pkg",
    ],
)

# bazel build c7n_gcp_wheel
# To install a generated whl-file into your env: pip install <WORKSPACE_directory>/bazel-bin/<file_name>.whl
# Installing c7n first is required for Custodian to work.
py_wheel_entry_points_ext(
    name = "c7n_gcp_wheel",
    distribution = "c7n_gcp",
    entry_points = {
        "custodian.resources": [
            "gcp = c7n_gcp.entry:initialize_gcp",
        ],
    },
    strip_path_prefixes = [
        "tools/c7n_gcp/",
    ],
    # the version is from tools/c7n_gcp/setup.py
    version = "0.3.8",
    deps = [
        "//tools/c7n_gcp/c7n_gcp:gcp_pkg",
    ],
)

# bazel build //:c7n_mailer_wheel
# To install a generated whl-file into your env: pip install <WORKSPACE_directory>/bazel-bin/<file_name>.whl
py_wheel(
    name = "c7n_mailer_wheel",
    console_scripts = {
        "c7n-mailer": "c7n_mailer.cli:main",
        "c7n-mailer-replay": "c7n_mailer.replay:main",
    },
    distribution = "c7n-mailer",
    strip_path_prefixes = [
        "tools/c7n_mailer/",
    ],
    # the version is from tools/c7n_mailer/setup.py
    version = "0.5.7",
    deps = [
        "//tools/c7n_mailer/c7n_mailer:c7n_mailer_pkg",
    ],
)

# bazel build //:c7n_kube_wheel
# To install a generated whl-file into your env: pip install <WORKSPACE_directory>/bazel-bin/<file_name>.whl
py_wheel_entry_points_ext(
    name = "c7n_kube_wheel",
    distribution = "c7n-kube",
    entry_points = {
        "custodian.resources": [
            "kube = c7n_kube.entry:initialize_kube",
        ],
    },
    strip_path_prefixes = [
        "tools/c7n_kube/",
    ],
    # the version is from tools/c7n_kube/setup.py
    version = "0.1.1",
    deps = [
        "//tools/c7n_kube/c7n_kube:c7n_kube_pkg",
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
    imports = [
        "tools/c7n_gcp",
    ],
    main = "//c7n:cli.py",
    deps = [
        "//c7n",
        "//tools/c7n_gcp/c7n_gcp:entry",
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
