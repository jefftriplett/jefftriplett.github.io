---
layout: page
title: Projects
permalink: /projects/
---

Most of my projects range from scratching personal itches, working on community projects and initiatives, and OSS projects.

{% for project in site.projects %}
### {{ project.title }}
{:.mt-8}
{{ project.content }}
{% endfor %}

### 100+ more projects on Github
{:.mt-8}

See more [projects on Github](https://github.com/jefftriplett).
