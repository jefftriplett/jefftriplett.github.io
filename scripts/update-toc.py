"""
Inspired by: https://github.com/HackSoftware/Django-Styleguide/blob/master/tools/update_toc.py
"""
import re
import typer

from pathlib import Path
from subprocess import check_output


TOC_BEGIN = "<!-- toc -->"
TOC_END = "<!-- tocstop -->"


def get_file_contents(filename):
    new_toc = check_output(f"markdown-toc {filename}", shell=True).decode("utf-8")

    pattern = [TOC_BEGIN, "", new_toc, "", TOC_END]

    return "\n".join(pattern)


def replace_toc(filename):
    text = Path(filename).read_text()
    new_toc = get_file_contents(filename)

    regex = f"{TOC_BEGIN}(.|\n)+{TOC_END}"

    new_text = re.sub(regex, new_toc, text)

    Path(filename).write_text(new_text)

    typer.echo("TOC updated ...")


def main(filename: str):
    return replace_toc(filename)


if __name__ == "__main__":
    typer.run(main)
