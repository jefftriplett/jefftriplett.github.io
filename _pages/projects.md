---
layout: default
title: Projects
permalink: /projects/
---

Most of my projects range from scratching personal itches, working on community projects and initiatives, and OSS projects.

{% for project in site.projects %}
### {{ project.title }}
{{ project.content }}
{% endfor %}

### 100+ more projects on Github

See more [projects on Github](https://github.com/jefftriplett).
