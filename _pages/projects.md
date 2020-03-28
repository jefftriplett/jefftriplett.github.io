---
layout: page
title: Projects
permalink: /projects/
---

Most of my projects range from scratching personal itches, working on community projects and initiatives, and OSS projects.

## Active Projects
{:.mt-6}

{% for project in site.projects %}
{% unless project.archived %}
<div class="mt-4">

<h3 class="-mb-4">{{ project.title }} 
    {% if project.github %}
    <span><a href="{{ project.github }}"><i class="fab fa-github" aria-hidden="true"></i></a></span>
    {% endif %}
    {% if project.homepage %}
    <span><a href="{{ project.homepage }}"><i class="far fa-home" aria-hidden="true"></i></a></span>
    {% endif %}
</h3>

<div class="text-gray-700"> 
{{ project.content }}
</div>

</div>
{% endunless %}
{% endfor %}

----

## Archived Projects
{:.mt-6}

{% for project in site.projects %}
{% if project.archived %}
<div class="mt-4">
<h3 class="-mb-4">{{ project.title }} 
    {% if project.github %}
    <span><a href="{{ project.github }}"><i class="fab fa-github" aria-hidden="true"></i></a></span>
    {% endif %}
    {% if project.homepage %}
    <span><a href="{{ project.homepage }}"><i class="far fa-home" aria-hidden="true"></i></a></span>
    {% endif %}
</h3>

<div class="text-gray-700"> 
{{ project.content }}
</div>

</div>
{% endif %}
{% endfor %}

----

### 100+ more projects on Github
{:.mt-8}

[See more projects on Github](https://github.com/jefftriplett).
{:.-mt-4 -mb-4}
