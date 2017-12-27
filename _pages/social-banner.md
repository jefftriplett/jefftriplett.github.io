---
layout: default
title: Social Media Banner
permalink: /social/
sitemap: false
---

## Contact / Social Media

Here are a few ways to keep up with me online. If you have a question about this project, please consider opening a GitHub Issue. 

{% for social in site.data.social.social %}{% if social.featured %}
[![]({{ social.icon }})]({{ social.url }}){% endif %}{% endfor %}

<textarea rows="10" style="width: 100%">{% raw %}
## Contact / Social Media

Here are a few ways to keep up with me online. If you have a question about this project, please consider opening a GitHub Issue. {% endraw %}
{% for social in site.data.social.social %}{% if social.featured %}
[![]({{ social.icon }})]({{ social.url }}){% endif %}{% endfor %}
</textarea>

----

## All Social Icons

{% for social in site.data.social.social %}[![]({{ social.icon }})]({{ social.url }})
{% endfor %}

<textarea rows="10" style="width: 100%">
{% for social in site.data.social.social %}[![]({{ social.icon }})]({{ social.url }})
{% endfor %}
</textarea>
