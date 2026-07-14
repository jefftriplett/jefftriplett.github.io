---
category: micro.blog
date: '2024-02-07T03:24:25.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: django-queryset-to-markdown-table
title: Django Queryset to Markdown Table
redirect_to: https://micro.webology.dev/2024/02/06/django-queryset-to-markdown-table/
tags:
- Django
- Python
---

Today, I asked on Mastodon if anyone knew of a good solution for generating a Markdown table from a Django queryset. Typically, people want to convert markdown into HTML, but this was a case where I needed to export data from Django to a static website.

Not missing a beat, [Katie McLaughlin](https://mastodon.social/@glasnt@cloudisland.nz/111886900012564229) recommended the [python-tabulate](https://github.com/astanin/python-tabulate) library, which is what I was looking for.

Since I was short on time tonight, I asked ChatGPT to:

1. Write a queryset to markdown function using the Python tabulate library.
2. Add Python types support (because it’s 2024)
3. Rewrite the docstring

Once the code looked right, I loaded up my local copy of [Django News Jobs](https://jobs.django-news.com), and I created a quick Django management command.

[django-click](https://github.com/GaretJax/django-click) is my go-to library for quickly writing CLI apps or what Django calls a management command. django-click reduces the boilerplate needed to write a management command down to one import, one decorator, and one function, and you get the best of the Python [click](https://click.palletsprojects.com/en/8.1.x/) library with everything Django has to offer.

```
# management/commands/table.py

import djclick as click

from django.db.models.query import QuerySet
from tabulate import tabulate

from jobs.models import JobListing


def queryset_to_markdown(queryset: QuerySet, fields: list[str] | None = None) -> str:
    """
    Convert a Django queryset to a markdown table using the tabulate library.

    Args:
        queryset (QuerySet): The Django queryset to convert into a markdown table.
        fields (list[str] | None, optional): A list of strings specifying the model fields to include in the table.
            If None, all fields from the model will be included. Defaults to None.

    Returns:
        str: A string representing the markdown table formatted according to GitHub-flavored Markdown.
    """

    # If fields are not specified, use all fields from the model
    if fields is None:
        fields = [field.name for field in queryset.model._meta.fields]

    # Prepare data for tabulation
    data = []
    for obj in queryset:
        row = [getattr(obj, field) for field in fields]
        data.append(row)

    # Generate markdown table
    markdown_table = tabulate(data, headers=fields, tablefmt="github")

    return markdown_table


@click.command()
def command():
    job_listings = JobListing.objects.all().active().order_by("-published")
    print(queryset_to_markdown(job_listings, fields=["title", "employer_name"]))
```

Running `python manage.py table` gave me the following table. Please note: I removed the `employer_name` column to fit the output in my article.



Overall, I’m happy with this approach. Django is an excellent framework for quickly prototyping and solving these problems.

I decided to write a management command instead of a view because markdown tables are very readable from the command line. I plan to convert it to a Django view to automate embedding tables like this into other projects.
