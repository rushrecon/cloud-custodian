package(default_visibility = ["//visibility:public"])

load("@rules_python//python:defs.bzl", "py_library")
load("@pip_deps//:requirements.bzl", "requirement")

py_library(
    name = "c7n_mailer_deps",
    deps = [
        requirement("boto3"),
        requirement("botocore"),
        requirement("docutils"),
        requirement("jmespath"),
        requirement("vcversioner"),
        requirement("Jinja2"),
        requirement("jsonschema"),
        requirement("ruamel.yaml"),
        requirement("six"),
        requirement("datadog"),
        requirement("sendgrid"),
        requirement("redis"),
        requirement("ldap3"),
        ":c7n_mailer_azure",
        ":c7n_mailer_other_srcs",
    ],
)

py_library(
    name = "c7n_mailer_cli",
    srcs = ["cli.py"],
    deps = [
        "@c7n_mailer//:c7n_mailer_deps",
    ],
)

py_library(
    name = "c7n_mailer_azure",
    srcs = glob(["azure_mailer/**/*"]),
)

py_library(
    name = "c7n_mailer_other_srcs",
    srcs = [
        "__init__.py",
        "datadog_delivery.py",
        "deploy.py",
        "email_delivery.py",
        "handle.py",
        "ldap_lookup.py",
        "replay.py",
        "slack_delivery.py",
        "smtp_delivery.py",
        "sns_delivery.py",
        "splunk_delivery.py",
        "sqs_queue_processor.py",
        "utils.py",
        "utils_email.py",
    ],
)
