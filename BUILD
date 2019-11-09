# Is required to run bazel from the root workspace.

# Making as much common parts as possible + adjusting bazel to a specific environment:
# 1. Remove this file from the repo, add it to .gitignore.
# 2. Write a manual where the procedure of this BUILD file creation is stated.
# 2.1. Using GCP? Add @c7n_gcp to the deps, create the required env files, then write a command referencing those files.

load("@com_github_atlassian_bazel_tools//:multirun/def.bzl", "command", "multirun")
load("@rules_python//python:defs.bzl", "py_binary", "py_library")

py_binary(
    name = "c7n_cli",
    srcs = ["@c7n//:cli.py"],
    data = glob(["env/*"]),
    main = "@c7n//:cli.py",
    deps = [
        "@c7n",
        "@c7n_gcp",
    ],
)

# The following looks cool and flexible enough.
# bazel run :c7n_gcp_cli env/gcp-sample.yml
command(
    name = "c7n_gcp_cli",
    arguments = [
        "run",
        # "env/gcp-sample.yml", # could also be specified but couples the command with a particular file.
        "--cache-period=0",
        "--output-dir=whatever",
    ],
    command = ":c7n_cli",
    environment = {
        "CLOUDSDK_CORE_PROJECT": "cloud-custodian-190204",
        "GOOGLE_APPLICATION_CREDENTIALS": "env/gcp-key.json",  # it is there in env, not committed.
    },
)
