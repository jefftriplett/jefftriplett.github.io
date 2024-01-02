---
layout: page
title: Projects
permalink: /projects/
---

Most of my projects range from scratching personal itches, working on community projects and initiatives, and open source projects.

----

## Active Projects

{% assign projects = site.projects | where:"archived", false | sort:"title" %}
<div class="grid grid-cols-3 gap-4">
{% for project in projects %}
{% include project.html project=project %}
{% endfor %}
</div>

----

## Archived Projects

{% assign projects = site.projects | where:"archived", true | sort:"title" %}
<div class="grid grid-cols-3 gap-4">
{% for project in projects %}
{% include project.html project=project %}
{% endfor %}
</div>

----

## 230+ more projects on GitHub

[See more projects on GitHub](https://github.com/jefftriplett)
