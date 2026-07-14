---
category: micro.blog
date: '2024-02-23T01:56:38.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: scratching-itches-with-python-and-chatgpt
title: Scratching Itches with Python and ChatGPT
redirect_to: https://micro.webology.dev/2024/02/22/scratching-itches-with-python-and/
tags:
- Django
- Python
- Today I Learned
---

A few times a week over the last several months, I have paired with ChatGPT to work on Python scripts that solve problems that I would otherwise have spent less time on. Some might feel too niche or even too tedious that I would otherwise not take the time to work on. Most of the time, these are scratching an itch and solving a problem on my mind.

Because of the time constraint, I have been impressed with the results. I usually spend 10 to 15 minutes prompting ChatGPT, then I spend 10 to 15 minutes refactoring the script, adding [Typer](https://typer.tiangolo.com), and refining the code. Sometimes, this involved copying all or parts of my script and pasting it back into ChatGPT to have it refine or refactor some section of code.

## YouTube Playlist to Markdown file

My [YouTube playlist to markdown script](https://gist.github.com/jefftriplett/4bf333453d7cab320aa45767b1949be6) is helpful for quickly getting a list of video URLs and titles back from a YouTube playlist. I have used this for DjangoCon US and a few other conferences to help collect links for social media and a few times for the [Django News Newsletter](https://django-news.com).

ChatGPT even documented the process, including links for how to set permissions for the YouTube API.

## Use Playwright to pull data out of the Django Admin

I have database access for most projects, but I recently needed to export a list of RSS feeds from the admin of a Django website. ChatGPT could quickly write a Playwright script to log in to the website, access a list page, and pull the feed field from the detail page. The script generated a JSON feed and could understand pagination and how to page through the links.

## GitHub Issues and Pull Request templates

For the [Awesome Django project](https://github.com/wsvincent/awesome-django), I asked ChatGPT to generate GitHub Issues and Pull Request templates based on my criteria. Once the templates were complete, I prompted ChatGPT to help me write a script that uses the GitHub API to read a pull request and validate the answers filled out while adding some other contextual data that makes it easier to verify the request.

## Modeling HTML with PyDantic

I am still trying to figure out what to do with the project, but I asked ChatGPT to use [Pydantic](https://github.com/pydantic/pydantic) to create a class that could represent HTML tags. Once I was happy with the API, I asked ChatGPT to represent all HTML tags. After a few more prompts, I could read, write, and represent an HTML document using this script using Pydantic.

## Outro

I’m still determining how useful these scripts are, but I have enjoyed these quick sessions to write a one-off script or to solve problems that come up a few times a year that never seemed worth the time spent trying to write it from scratch.
