OutputDocs = provider(fields = ["files", "name"])

#   Generating rst files from classes
def _impl(ctx):
    tree = ctx.actions.declare_directory(ctx.attr.provider + "/resources")

    ctx.actions.run(
        inputs = [],
        outputs = [tree],
        #   Set arguments for main in docgen.py
        arguments = [tree.path, ctx.attr.provider, ctx.attr.resource_type],
        executable = ctx.executable.tool,
    )

    return [OutputDocs(files = depset([tree]), name = ctx.attr.provider)]

#   Copying external and generated files, generate html docs
def _impl2(ctx):
    ext_docs = ctx.actions.declare_directory("docs/")
    source = "/source"
    tools = "/tools"
    doctrees = ctx.actions.declare_directory("build/doctrees")
    html = ctx.actions.declare_directory("build/html")

    inputs = []
    commands = []
    directories = []

    #   Make commands for create directories
    for file in ctx.files.srcs:
        inputs.append(file)
        if file.dirname not in directories:
            directories.append(file.dirname)
            commands.append(
                "mkdir -p %s/%s" % (ext_docs.dirname, file.dirname),
            )

    #   Make commands for copy external files from docs
    for file in ctx.files.srcs:
        commands.append(
            "cp %s %s/%s" % (file.path, ext_docs.dirname, file.dirname),
        )

    #   Rename readme.md files and make commands for copy,
    #   and make dir and copy file for docs/source/tools
    for file in ctx.files.copy:
        inputs.append(file)
        if file.basename.lower() >= "readme.md":
            name = file.dirname.split("/")[-1].replace("_", "-") + ".md"
            path = ext_docs.path + source + tools + "/" + name
            commands.append(
                "cp %s %s" % (file.path, path),
            )
        else:
            path = ext_docs.path + source + tools + "/" + file.dirname.split("/")[-1]
            commands.append(
                "mkdir -p %s && cp %s %s" % (path, file.path, path),
            )

    #   Make commands for create directories and copy generated files
    for src in ctx.attr.inputs:
        input_depset = src[OutputDocs].files
        list = src[OutputDocs].files.to_list()
        commands.append(
            "mkdir -p %s%s/%s && cp -R %s \"$_\"" % (ext_docs.path, source, src[OutputDocs].name, list[0].path),
        )
        inputs.append(list[0])

    #   Run commands
    ctx.actions.run_shell(
        inputs = depset(inputs),
        outputs = [ext_docs],
        command = "\n".join(commands),
    )

    #   Run generating html docs
    ctx.actions.run(
        inputs = [ext_docs],
        outputs = [doctrees, html],
        #   Arguments for sphinx-build
        arguments = ["-W", "-j", "auto", "-b", "html", "-d", doctrees.path, ext_docs.path + source, html.path],
        executable = ctx.executable.tool,
    )

    return [DefaultInfo(files = depset([doctrees, html]))]

def _impl3(ctx):
    return [DefaultInfo(files = depset(ctx.files.srcs))]

foo = rule(
    implementation = _impl,
    attrs = {
        #   Run docgen.py
        "tool": attr.label(
            executable = True,
            cfg = "host",
            allow_files = True,
        ),
        #   Attribute provider for main in docgen.py
        "provider": attr.string(
            mandatory = True,
        ),
        #   Attribute resource_type for main in docgen.py
        "resource_type": attr.string(
            mandatory = True,
        ),
    },
)

foo2 = rule(
    implementation = _impl2,
    attrs = {
        #    Run sphinx-build.py
        "tool": attr.label(
            executable = True,
            cfg = "host",
            allow_files = True,
        ),
        #   Generated files from classes
        "inputs": attr.label_list(
            allow_empty = False,
        ),
        #   Collected all files from docs
        "srcs": attr.label_list(
            allow_empty = False,
            allow_files = True,
        ),
        #   Collected readme.md from tools
        "copy": attr.label_list(
            allow_empty = False,
            allow_files = True,
        ),
    },
)

#   For collecting external files
foo_library = rule(
    implementation = _impl3,
    attrs = {
        "srcs": attr.label_list(allow_files = True),
    },
)
