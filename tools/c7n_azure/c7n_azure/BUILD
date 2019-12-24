load("@my_sphinx_deps//:requirements.bzl", "requirement")

py_library(
    name = "c7n_azure",
    srcs = glob(["**/*.py"]),
    visibility = ["//visibility:public"],
    deps = [
        requirement("adal"),
        requirement("msrestazure"),
        requirement("msrest"),
        requirement("isodate"),
        requirement("netaddr"),
        requirement("applicationinsights"),
        requirement("jsonpickle"),
    ],
)
