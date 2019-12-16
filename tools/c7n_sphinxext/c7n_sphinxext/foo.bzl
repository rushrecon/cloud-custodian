OutputDocs = provider(fields = ["files", "name"])

def _impl(ctx):
    tree = ctx.actions.declare_directory(ctx.attr.provider + "/resources")
    print("foo. tree path - %s" % tree.path)

    ctx.actions.run(
        inputs = [],
        outputs = [tree],
        arguments = [tree.path, ctx.attr.provider, ctx.attr.resource_type],
        progress_message = "Generating folder into '%s'" % tree.path,
        executable = ctx.executable.tool,
    )

    return [OutputDocs(files = depset([tree]), name = ctx.attr.provider)]

#    return [DefaultInfo(files = depset([tree]))]

def _impl2(ctx):
    source = ctx.actions.declare_directory("docs/source/")  #aws/
    doctrees = ctx.actions.declare_directory("docs/build/doctrees")
    html = ctx.actions.declare_directory("docs/build/html")

    print("foo2. source path - %s" % source.path)

    commands = []
    inputs = []

    for src in ctx.attr.inputs:
        input_depset = src[OutputDocs].files
        list = src[OutputDocs].files.to_list()
        commands.append(
            "mkdir %s/%s && cp -R %s \"$_\"" % (source.path, src[OutputDocs].name, list[0].path),
        )
        inputs.append(list[0])

    ext_file = []
    for f in ctx.attr.ext_files:
        ext_file.append(f)
        print(f)

    ctx.actions.run_shell(
        inputs = depset(inputs),
        outputs = [source],
        command = "\n".join(commands),
    )

    ctx.actions.run(
        inputs = [source],
        outputs = [doctrees, html],
        arguments = ["-W", "-j", "auto", "-b", "html", "-d", doctrees.path, source.path, html.path],
        executable = ctx.executable.tool,
    )

    return [DefaultInfo(files = depset([doctrees, html]))]

foo = rule(
    implementation = _impl,
    attrs = {
        "tool": attr.label(
            executable = True,
            cfg = "host",
            allow_files = True,
        ),
        "provider": attr.string(
            mandatory = True,
        ),
        "resource_type": attr.string(
            mandatory = True,
        ),
        "sphinx": attr.label(
            executable = True,
            cfg = "host",
            allow_files = True,
        ),
    },
)

foo2 = rule(
    implementation = _impl2,
    attrs = {
        "tool": attr.label(
            executable = True,
            cfg = "host",
            allow_files = True,
        ),
        "inputs": attr.label_list(
            allow_empty = False,
        ),
        "ext_files": attr.label_list(
            allow_empty = False,
            allow_files = True,
        ),
    },
)
