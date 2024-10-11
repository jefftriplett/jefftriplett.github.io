---
layout: page
title: Projects
permalink: /projects/
---

<p class="text-4xl">Most of my projects range from scratching personal itches, working on community projects and initiatives, and open source projects.</p>

----

## Active Projects

{% assign projects = site.projects | where:"archived", false | sort:"title" %}
<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
{% for project in projects %}
{% include project.html project=project %}
{% endfor %}
</div>

----

## Archived Projects

{% assign projects = site.projects | where:"archived", true | sort:"title" %}
<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
{% for project in projects %}{% include project.html project=project %}
{% endfor %}
</div>

----

## 230+ more projects on GitHub

[See more projects on GitHub](https://github.com/jefftriplett)
