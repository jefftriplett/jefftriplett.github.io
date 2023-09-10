---
layout: page
title: Projects
permalink: /projects/
---

Most of my projects range from scratching personal itches, working on community projects and initiatives, and open source projects.

----

## Active Projects

{% assign projects = site.projects | where:"archived", false | sort:"title" %}
{% for project in projects %}
{% include project.html project=project %}
{% endfor %}

----

## Archived Projects

{% assign projects = site.projects | where:"archived", true | sort:"title" %}
{% for project in projects %}
{% include project.html project=project %}
{% endfor %}

----

## 230+ more projects on GitHub

[See more projects on GitHub](https://github.com/jefftriplett)
