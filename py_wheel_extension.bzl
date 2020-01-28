load("@rules_python//experimental/python:wheel.bzl", "py_package", "py_wheel")


def _impl_a(ctx):
    inputs = ctx.attr.whl_file.data_runfiles.files.to_list()
    out_file = ctx.outputs.output
    contents = []
    args = ctx.actions.args()
    for k, v in ctx.attr.entry_points.items():
        contents.append("[%s]" % k)
        for p in v:
            contents.append(p)
    contents = "\\n".join(contents)
    ctx.actions.run_shell(
        inputs = inputs,
        outputs = [out_file],
        command ="%s/add-entry-points-to-wheel.sh '%s' '%s' '%s' '%s'"  % (
            ctx.var["path"], ctx.attr.distr_info,  inputs[0].path, contents, out_file.path
        ),

    )


_add_entry_points = rule(
    implementation = _impl_a,
    attrs = {
        "entry_points": attr.string_list_dict(mandatory=True),
        "distr_info": attr.string(mandatory=True),
        "whl_file": attr.label(mandatory = True),
        "output": attr.output(doc = "The generated file"),
    },
)



def py_wheel_entry_points_ext(**kwargs):
    if kwargs.get("entry_points"):
        entry_points = kwargs.pop("entry_points")
    else:
        fail("Entry points not specified")
    py_wheel_rule_name = kwargs["name"] + "_wheel"
    py_wheel(
        name = py_wheel_rule_name,
        distribution = kwargs["distribution"],
        strip_path_prefixes = kwargs["strip_path_prefixes"],
        version = kwargs["version"],
        deps = kwargs["deps"],
    )
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
    _add_entry_points(
        name = kwargs["name"] ,
        entry_points=entry_points,
        distr_info =  kwargs["distribution"] + "-" +kwargs["version"],
        whl_file = "//:"+ py_wheel_rule_name,
        output=outfile
    )

