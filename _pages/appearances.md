---
layout: page
permalink: /appearances/
title: "Appearances"
---

<p class="text-4xl font-light text-gray-700 dark:text-gray-300">Podcasts, interviews, and other <span class="text-purple-600 dark:text-purple-400">appearances</span> I've made over the years.</p>

<div class="my-8 border-t border-gray-200 dark:border-gray-700"></div>

{% assign sorted_appearances = site.appearances | sort: 'date' | reverse %}
<div class="grid grid-cols-1 gap-4 my-6">
{% for appearance in sorted_appearances %}
{% include appearance.html appearance=appearance %}
{% endfor %}
</div>
