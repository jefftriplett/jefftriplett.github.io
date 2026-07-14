---
category: micro.blog
date: '2024-08-22T03:57:49.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: uv-updates-and-pep-723-simplifying-python-packaging-and
title: '🐍 UV Updates and PEP 723: Simplifying Python Packaging and Scripting'
redirect_to: https://micro.webology.dev/2024/08/21/uv-updates-and-pep-simplifying/
tags:
- Python
- UV
---

The [uv: Unified Python packaging](https://astral.sh/blog/uv-unified-python-packaging) update brings fresh air to the Python community, with several improvements streamlining the development process. One exciting addition is an early preview of [PEP 723](https://peps.python.org/pep-0723/), also known as [Single-file scripts](https://astral.sh/blog/uv-unified-python-packaging#single-file-scripts).

The Single-file scripts feature particularly caught my attention due to its potential to simplify the distribution and execution of small Python projects. Streamlining the process is highly appealing to someone who frequently creates GitHub Gists and shares them privately and publicly.

With this new feature, I can now instruct users to run `uv run main.py` without explaining what a `venv` or `virtualenv` is, plus a long list of requirements that need to be passed to `pip install`.

I had the opportunity to test this feature over lunch today. While adding libraries to the script was straightforward, I encountered a few hurdles when I forgot to invoke `uv run` in my virtual environment (venv). This makes sense, given that it’s a new habit, but it highlights the importance of adapting to changes in our development workflow.

Overall, the UV: Unified Python packaging update and the introduction of Single-file scripts mark a significant step in simplifying Python development. As developers become more familiar with these improvements, we expect increased adoption and smoother collaboration on small-scale projects.

## Bonus Example

I looked through some of my recent visits, and one I recently shared with a few conference organizer friends was a one-off script I used to read several YouTube video JSON files that I’m using to bootstrap another project. It was the first time I used [DuckDB](https://duckdb.org) to make quick work of reading data from a bunch of JSON files using SQL.

Overall, I was happy with DuckDB and what PEP 723 might bring to the future of Python apps, even if my example only does a little.

```
# To run this application, use:
#   uv run demo-duckdb.py
#
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "duckdb",
#     "rich",
#     "typer",
# ]
# ///
import duckdb
import typer

from rich import print


def main():
    result = duckdb.sql("SELECT id,snippet FROM read_json('json/*.json')").fetchall()

    for row in result:
        id, snippet = row
        print("-" * 80)
        print(f"{id=}")
        print(f"{snippet['channelTitle']=}")
        print(f"{snippet['title']=}")
        print(f"{snippet['publishedAt']=}")
        print(snippet["description"])
        print(snippet["thumbnails"].get("maxres") or snippet.get("standard"))
        print()


if __name__ == "__main__":
    typer.run(main)
```

Overall, the future is bright with UV and PEP 723 may bring us. I’m excited to have more one-file Python apps that are easier to share and run with others.

PEP 723 also opens the door to turning a one-file Python script into a runnable Docker image that doesn’t even need Python on the machine or opens the door for [Beeware](https://beeware.org) and [Briefcase](https://beeware.org/project/projects/tools/briefcase/) to build standalone apps.
