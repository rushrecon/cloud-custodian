load("@rules_python//experimental/python:wheel.bzl", "py_package", "py_wheel")
#
#
def _impl(ctx):
    out=""
    contents = []
    for k, v in ctx.attr.entry_points.items():
        contents.append("[%s]" % k)
        for p in v:
            contents.append(p)
        contents.append("\n")
    contents = "\n".join(contents)
    ctx.actions.run_shell(
        command ="add-entry-points-to-wheel.sh %s %s %s"  % (
            contents, ctx.attr.whl_file, ctx.attr.distr_info
        ),
    )
    return [DefaultInfo(
        outfile=[out]
    )]
#
_add_entry_points = rule(
    implementation = _impl,
    executable = True,
    attrs = {
        "entry_points": attr.string_list_dict(mandatory=True),
        "distr_info": attr.string(mandatory=True),
        "whl_file": attr.string(mandatory=True),
    },
)


def py_wheel_ext(**kwargs):
    py_wheel(**kwargs)
    # TODO: Find a way to get an output file of the previous rule
    outfile = "bazel-bin/" + "-".join(
        [
            kwargs["distribution"],
            kwargs["version"],
            "py3",
            "none",
            "any",
        ]
    ) + ".whl"
    if kwargs.get("entry_points"):
        _add_entry_points(
            name = "add_entry_points",
            entry_points=kwargs["entry_points"],
            distr_info =  kwargs["distribution"] + "-" +kwargs["version"],
            whl_file = outfile
        )


