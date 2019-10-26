py_library(
    name = "custodian-test",
    srcs = ["c7n/version.py"],
)

py_binary(
    name = "custodian-test-bin",
    srcs = ["c7n/version-main.py"],
    main = "c7n/version-main.py",
    deps = [":custodian-test"],
)
