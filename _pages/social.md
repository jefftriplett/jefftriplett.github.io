---
layout: default
title: Social Media Banner
permalink: /social/
sitemap: false
---

## Contact / Social Media

Here are a few ways to keep up with me online. If you have a question about this project, please consider opening a GitHub Issue. 

{% assign social_sorted = site.data.social.social | sort: 'order', 'last' %}

{% for social in social_sorted %}{% if social.featured %}
[![]({{ social.icon }})]({{ social.url }}){% endif %}{% endfor %}

Made with :heart: in Lawrence, KS USA

<script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/1.7.1/clipboard.min.js"></script>

<textarea id="simple" rows="10" style="width: 100%">{% raw %}
## Contact / Social Media

Here are a few ways to keep up with me online. If you have a question about this project, please consider opening a GitHub Issue. {% endraw %}
{% for social in social_sorted %}{% if social.featured %}
[![]({{ social.icon }})]({{ social.url }}){% endif %}{% endfor %}

{% raw %}Made with :heart: in Lawrence, KS USA{% endraw %}
</textarea>
<button class="btn" data-clipboard-action="copy" data-clipboard-target="#simple">
    Copy to clipboard
</button>

----

## All Social Icons

{% for social in site.data.social.social %}[![]({{ social.icon }})]({{ social.url }})
{% endfor %}

<textarea id="all" rows="10" style="width: 100%">
{% for social in site.data.social.social %}[![]({{ social.icon }})]({{ social.url }})
{% endfor %}
</textarea>
<button class="btn" data-clipboard-action="copy" data-clipboard-target="#all">
    Copy to clipboard
</button>

<script>
    new Clipboard('.btn');
</script>
