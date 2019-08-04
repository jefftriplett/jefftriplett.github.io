---
layout: page
title: Projects
permalink: /projects/
---

Most of my projects range from scratching personal itches, working on community projects and initiatives, and OSS projects.

{% for project in site.projects %}
### {{ project.title }} {% if project.github %}<span><a href="{{ project.github }}"><i class="fab fa-github" aria-hidden="true"></i></a></span>{% endif %} {% if project.homepage %}<span><a href="{{ project.homepage }}"><i class="far fa-home" aria-hidden="true"></i></a></span>{% endif %}
{:.mt-8 .-mb-4}
{{ project.content }}
{% endfor %}

### 100+ more projects on Github
{:.mt-8 .-mb-4}

[See more projects on Github](https://github.com/jefftriplett).
