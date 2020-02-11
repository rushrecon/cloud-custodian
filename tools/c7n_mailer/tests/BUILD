load("//:c7n_py_test.bzl", "c7n_py_test")
load("@pip_deps//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:private"])

# TODO: get rid of excluded tests
# All three complaining about azure.xxx imports.
EXCLUDED_AZURE_TESTS = [
    # "test_azure.py",
    # "test_azure_mailer_utils.py",
    # "test_utils.py",
]

py_library(
    name = "test_data",
    data = glob(["test-templates/*.j2"]),
)

py_library(
    name = "test_deps",
    srcs = ["common.py"],
    data = ["example.jinja"],
    deps = [
        ":test_data",
        "//c7n",
        "//tools/c7n_azure/c7n_azure:c7n_azure_lib",
        requirement("mock"),
        requirement("fakeredis"),
        requirement("attrs"),
        requirement("pytest"),
        requirement("pyrsistent"),
        requirement("pluggy"),
        requirement("sortedcontainers"),
        requirement("pyasn1"),
        requirement("importlib_metadata"),
        requirement("zipp"),
        requirement("py"),
        requirement("packaging"),
        requirement("more_itertools"),
        requirement("jsonpointer"),
        requirement("jsonpatch"),
        requirement("python_http_client"),
        requirement("PyJWT"),
    ],
)

[c7n_py_test(
    name = test_file[:-3],
    srcs = [test_file],
    imports = [
        ".",
        "..",
        "../../c7n_azure/.",
    ],
    main = test_file,
    srcs_version = "PY2AND3",
    deps = [
        ":test_deps",
        "//tools/c7n_mailer/c7n_mailer:c7n_mailer_cli",  # used instead of c7n_mailer_core_deps for testing cli as well
        "//tools/c7n_azure/c7n_azure:storage_utils",
        #        "//tools/c7n_azure/c7n_azure:storage_utils",
        "//tools/c7n_azure/c7n_azure:c7n_azure_lib",
    ],
) for test_file in glob(
    include = ["test_*.py"],
    exclude = EXCLUDED_AZURE_TESTS,
)]

# bazel test //tools/c7n_mailer/tests
test_suite(
    name = "tests",
)
