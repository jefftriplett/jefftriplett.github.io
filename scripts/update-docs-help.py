"""
Inspired by: https://github.com/simonw/datasette/blob/master/update-docs-help.py
"""
from pathlib import Path
from subprocess import check_output

# docs_path = Path(__file__).parent / "docs"

# includes = (
#     ("serve", "datasette-serve-help.txt"),
#     ("package", "datasette-package-help.txt"),
#     ("publish nowv1", "datasette-publish-nowv1-help.txt"),
#     ("publish heroku", "datasette-publish-heroku-help.txt"),
#     ("publish cloudrun", "datasette-publish-cloudrun-help.txt"),
# )


# def update_help_includes():
#     for name, filename in includes:
#         runner = CliRunner()
#         result = runner.invoke(cli, name.split() + ["--help"], terminal_width=88)
#         actual = "$ datasette {} --help\n\n{}".format(name, result.output)
#         actual = actual.replace("Usage: cli ", "Usage: datasette ")
#         open(docs_path / filename, "w").write(actual)


def main():
    filenames = Path(
        "..",
        "jefftriplett-examples-git",
        "django-baker-example",
    ).glob("**/*.sh")
    for filename in filenames:
        print(filename)
        contents = check_output(f"{filename}", shell=True).decode("utf-8")
        Path(f"{filename}.txt").write_text(contents)
        print(contents)


if __name__ == "__main__":
    main()
