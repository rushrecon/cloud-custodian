py_binary(
    name = "c7n_sphinxext_docgen",
    srcs = ["docgen.py"],
    data = glob(["_templates/*.rst"]),
    imports = [
        "..",
        "../../c7n_azure",
        "../../c7n_gcp",
    ],
    main = "docgen.py",
    deps = [
        ":sphinxlib",
        "//c7n",
        "//tools/c7n_azure/c7n_azure",
        "//tools/c7n_gcp/c7n_gcp",
    ],
)

py_binary(
    name = "sphinx_build",
    srcs = ["@my_sphinx_deps_pypi__Sphinx_2_2_1//:sphinx/cmd/build.py"],
    imports = [
        "..",
        "../../c7n_azure",
        "../../c7n_gcp",
    ],
    main = "@my_sphinx_deps_pypi__Sphinx_2_2_1//:sphinx/cmd/build.py",
    deps = [
        ":c7n_sphinxext",
        ":sphinxlib",
        "//c7n",
        "//tools/c7n_azure/c7n_azure",
        "//tools/c7n_gcp/c7n_gcp",
    ],
)

load(":foo.bzl", "foo", "foo2")

foo(
    name = "aws_gen",
    provider = "aws",
    resource_type = "resource_type.service",
    tool = ":c7n_sphinxext_docgen",
)

foo(
    name = "gcp_gen",
    provider = "gcp",
    resource_type = "resource_type.service",
    tool = ":c7n_sphinxext_docgen",
)

foo(
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
    inputs = [
        ":aws_gen",
        ":gcp_gen",
        ":azure_gen",
    ],
    tool = ":sphinx_build",
)

load("@my_sphinx_deps//:requirements.bzl", "requirement")

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
