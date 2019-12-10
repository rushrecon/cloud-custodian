# Solely for requirements.txt.
# bazel run //tools/c7n_gcp:gcp_develop
py_binary(
    name = "gcp_develop",
    srcs = ["setup.py"],
    args = ["develop"],
    data = ["readme.md"],
    main = "setup.py",
)
