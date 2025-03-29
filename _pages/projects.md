---
layout: page
title: Projects
permalink: /projects/
---

<p class="text-4xl font-light text-gray-700 dark:text-gray-300">Most of my projects range from <span class="text-emerald-600 dark:text-emerald-400">scratching personal itches</span>, working on <span class="text-amber-600 dark:text-amber-400">community projects and initiatives</span>, and <span class="text-indigo-600 dark:text-indigo-400">open source projects</span>.</p>

----

## <span class="text-emerald-600 dark:text-emerald-400">Active Projects</span>

{% assign projects = site.projects | where:"archived", false | sort:"title" %}
<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
{% for project in projects %}
{% include project.html project=project %}
{% endfor %}
</div>

----

## <span class="text-amber-600 dark:text-amber-400">Archived Projects</span>

{% assign projects = site.projects | where:"archived", true | sort:"title" %}
<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
{% for project in projects %}{% include project.html project=project %}
{% endfor %}
</div>

----

## <span class="text-indigo-600 dark:text-indigo-400">230+ more projects on GitHub</span>

<a href="https://github.com/jefftriplett" class="inline-block px-4 py-2 font-medium text-white bg-indigo-600 rounded-md hover:bg-indigo-700 transition-colors duration-200 dark:bg-indigo-700 dark:hover:bg-indigo-800">See more projects on GitHub <span class="ml-1">→</span></a>
