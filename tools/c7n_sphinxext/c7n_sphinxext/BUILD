load("@my_sphinx_deps//:requirements.bzl", "requirement")
load(":foo.bzl", "foo2", "rst_files_gen")
load("//:builddefs.bzl", "EXCLUDED_PKGS")

EXCLUDED_PKGS = [
    "azure_cosmosdb_nspkg",
]

SPHINX_REPO_PATH_FMT = requirement("Sphinx").split(":")[0] + ":%s"

py_binary(
    name = "c7n_sphinxext_docgen",
    srcs = ["docgen.py"],
    data = glob(["_templates/*.rst"]),
    imports = [
        "..",
        "../../c7n_azure",
        "../../c7n_gcp",
        "../../c7n_kube",
    ],
    main = "docgen.py",
    deps = [
        ":sphinxlib",
        "//c7n",
        "//tools/c7n_azure/c7n_azure:c7n_azure_lib",
        "//tools/c7n_gcp/c7n_gcp:entry",
        "//tools/c7n_kube/c7n_kube:kube_lib",
    ],
)

py_binary(
    name = "sphinx_build",
    srcs = [SPHINX_REPO_PATH_FMT % "sphinx/cmd/build.py"],
    imports = [
        "..",
        "../../c7n_azure",
        "../../c7n_gcp",
        "../../c7n_kube",
    ],
    main = SPHINX_REPO_PATH_FMT % "sphinx/cmd/build.py",
    deps = [
        ":c7n_sphinxext",
        ":sphinxlib",
        "//c7n",
        "//tools/c7n_azure/c7n_azure:c7n_azure_lib",
        "//tools/c7n_gcp/c7n_gcp:entry",
        "//tools/c7n_kube/c7n_kube:kube_lib",
    ],
)

rst_files_gen(
    name = "aws_gen",
    provider = "aws",
    resource_type = "resource_type.service",
    tool = ":c7n_sphinxext_docgen",
)

rst_files_gen(
    name = "gcp_gen",
    provider = "gcp",
    resource_type = "resource_type.service",
    tool = ":c7n_sphinxext_docgen",
)

rst_files_gen(
    name = "azure_gen",
    provider = "azure",
    resource_type = "resource_type.doc_groups",
    tool = ":c7n_sphinxext_docgen",
)

# bazel build //tools/c7n_sphinxext/c7n_sphinxext:sphinx_gen
foo2(
    name = "sphinx_gen",
    srcs = ["//:ext_files"],
    copy = ["//:copy_from_tools"],
    excluded_pkgs = EXCLUDED_PKGS,
    inputs = [
        ":aws_gen",
        #        ":gcp_gen",
        #        ":azure_gen",
    ],
    tool = ":sphinx_build",
)

py_library(
    name = "sphinxlib",
    deps = [
        requirement("Sphinx"),
        requirement("click"),
        requirement("recommonmark"),
        requirement("sphinx_rtd_theme"),
        requirement("imagesize"),
        requirement("sphinx-markdown-tables"),
        requirement("alabaster"),
        requirement("commonmark"),
        requirement("markdown"),
        requirement("chardet"),
        requirement("requests"),
        requirement("idna"),
        requirement("python-dateutil"),
        requirement("futures"),
        requirement("jinja2"),
        requirement("markupsafe"),
        requirement("babel"),
        requirement("pytz"),
        requirement("attrs"),
        requirement("pyrsistent"),
        requirement("importlib_metadata"),
        requirement("zipp"),
        requirement("more_itertools"),
        requirement("docutils"),
        requirement("pygments"),
        requirement("packaging"),
    ],
)

py_library(
    name = "c7n_sphinxext",
    srcs = glob(["*.py"]),
    data = glob(["_templates/*.rst"]),
)
