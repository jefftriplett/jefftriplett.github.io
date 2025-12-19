---
layout: page
title: AI Agents
permalink: /agents/
---

<p class="text-4xl font-light text-gray-700 dark:text-gray-300">I've been experimenting with building <span class="text-purple-600 dark:text-purple-400">AI agents</span> that help with <span class="text-emerald-600 dark:text-emerald-400">development workflows</span>, <span class="text-amber-600 dark:text-amber-400">code analysis</span>, and <span class="text-indigo-600 dark:text-indigo-400">automation tasks</span>.</p>

<div class="my-8 border-t border-gray-200 dark:border-gray-700"></div>

## <span class="text-purple-600 dark:text-purple-400">Active Agents</span>

{% assign agents = site.agents | where:"archived", false | sort:"title" %}
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 my-6">
{% for agent in agents %}
{% include agent.html agent=agent %}
{% endfor %}
</div>

<div class="my-8 border-t border-gray-200 dark:border-gray-700"></div>

## <span class="text-amber-600 dark:text-amber-400">Archived Agents</span>

{% assign agents = site.agents | where:"archived", true | sort:"title" %}
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 my-6">
{% for agent in agents %}
{% include agent.html agent=agent %}
{% endfor %}
</div>

<div class="my-8 border-t border-gray-200 dark:border-gray-700"></div>

## <span class="text-indigo-600 dark:text-indigo-400">More experiments on GitHub</span>

<div class="my-6 text-center">
  <a href="https://github.com/jefftriplett" class="inline-block px-6 py-3 font-medium text-white bg-purple-600 rounded-lg hover:bg-purple-700 transition-all duration-200 shadow-md hover:shadow-lg dark:bg-purple-700 dark:hover:bg-purple-800">
    <i class="fab fa-github mr-2" aria-hidden="true"></i>See more experiments on GitHub <span class="ml-1">→</span>
  </a>
</div>
