---
layout: page
title: AI Agents
permalink: /agents/
---

<p class="text-4xl font-light text-gray-700 dark:text-gray-300">I've been experimenting with building <span class="text-purple-600 dark:text-purple-400">AI agents</span> that help with <span class="text-emerald-600 dark:text-emerald-400">development workflows</span>, <span class="text-amber-600 dark:text-amber-400">code analysis</span>, and <span class="text-indigo-600 dark:text-indigo-400">automation tasks</span>.</p>

<div class="my-8 border-t border-gray-200 dark:border-gray-700"></div>

## <span class="text-purple-600 dark:text-purple-400">Active Agents</span>

{% if site.agents %}
{% assign active_agents = site.agents | where:"archived", false | sort:"title" %}
{% if active_agents.size > 0 %}
<div class="my-6 space-y-4">
{% for agent in active_agents %}
  <div class="border-b border-gray-200 dark:border-gray-700 pb-4 last:border-b-0">
    <h3 class="text-lg font-semibold text-gray-800 dark:text-gray-200 mb-2">
      {% if agent.github %}
        <a href="{{ agent.github }}" class="text-purple-600 dark:text-purple-400 hover:text-purple-800 dark:hover:text-purple-300">{{ agent.title }}</a>
        {% elsif agent.homepage %}
        <a href="{{ agent.homepage }}" class="text-purple-600 dark:text-purple-400 hover:text-purple-800 dark:hover:text-purple-300">{{ agent.title }}</a>
        {% elsif agent.blog_post %}
        <a href="{{ agent.blog_post }}" class="text-purple-600 dark:text-purple-400 hover:text-purple-800 dark:hover:text-purple-300">{{ agent.title }}</a>
      {% else %}
        {{ agent.title }}
      {% endif %}
      <span class="ml-2 text-sm">
        {% if agent.github %}
          <a href="{{ agent.github }}" class="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200">
            <i class="fab fa-github" aria-hidden="true"></i>
          </a>
        {% endif %}
        {% if agent.homepage %}
          <a href="{{ agent.homepage }}" class="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200 ml-2">
            <i class="fas fa-external-link-alt" aria-hidden="true"></i>
          </a>
        {% endif %}
        {% if agent.blog_post %}
          <a href="{{ agent.blog_post }}" class="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200 ml-2">
            <i class="fas fa-blog" aria-hidden="true"></i>
          </a>
        {% endif %}
      </span>
    </h3>
    <p class="text-gray-700 dark:text-gray-300">{{ agent.content | strip_html }}</p>
  </div>
{% endfor %}
</div>
{% else %}
<p class="text-gray-600 dark:text-gray-400">No active agents yet. Check back soon!</p>
{% endif %}
{% else %}
<p class="text-gray-600 dark:text-gray-400">No agents collection found.</p>
{% endif %}

<div class="my-8 border-t border-gray-200 dark:border-gray-700"></div>

## <span class="text-amber-600 dark:text-amber-400">Archived Agents</span>

{% if site.agents %}
{% assign archived_agents = site.agents | where:"archived", true | sort:"title" %}
{% if archived_agents.size > 0 %}
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 my-6">
{% for agent in archived_agents %}
{% include agent.html agent=agent %}
{% endfor %}
</div>
{% else %}
<p class="text-gray-600 dark:text-gray-400">No archived agents.</p>
{% endif %}
{% else %}
<p class="text-gray-600 dark:text-gray-400">No agents collection found.</p>
{% endif %}

<div class="my-8 border-t border-gray-200 dark:border-gray-700"></div>

## <span class="text-indigo-600 dark:text-indigo-400">More AI Experiments</span>

{% assign agents_posts = site.posts | where_exp: "post", "post.tags contains 'agents'" %}
{% assign llm_posts = site.posts | where_exp: "post", "post.tags contains 'llm'" %}
{% assign ai_posts_tagged = site.posts | where_exp: "post", "post.tags contains 'ai'" %}
{% assign ai_posts = agents_posts | concat: llm_posts | concat: ai_posts_tagged | uniq | sort: 'date' | reverse %}
{% if ai_posts.size > 0 %}
<div class="grid grid-cols-1 gap-4 my-6">
{% for post in ai_posts limit:5 %}
  <article class="flex flex-col p-4 bg-gray-50 rounded-lg border border-gray-200 dark:bg-gray-800 dark:border-gray-700">
    <h3 class="text-lg font-semibold mb-2">
      <a href="{{ post.url }}" class="text-indigo-600 dark:text-indigo-400 hover:text-indigo-800 dark:hover:text-indigo-300">
        {{ post.title }}
      </a>
    </h3>
    <time class="text-sm text-gray-600 dark:text-gray-400 mb-2">{{ post.date | date: "%B %e, %Y" }}</time>
    {% if post.excerpt %}
      <p class="text-gray-700 dark:text-gray-300">{{ post.excerpt | strip_html | truncate: 200 }}</p>
    {% endif %}
  </article>
{% endfor %}
</div>

<div class="my-6 text-center">
  <a href="?tags=agents,llm" class="inline-block px-6 py-3 font-medium text-white bg-indigo-600 rounded-lg hover:bg-indigo-700 transition-all duration-200 shadow-md hover:shadow-lg dark:bg-indigo-700 dark:hover:bg-indigo-800">
    View all AI posts <span class="ml-1">→</span>
  </a>
</div>
{% else %}
<p class="text-gray-600 dark:text-gray-400 my-6">No AI-related blog posts found yet.</p>
{% endif %}

<div class="my-6 text-center">
  <a href="https://github.com/jefftriplett" class="inline-block px-6 py-3 font-medium text-white bg-purple-600 rounded-lg hover:bg-purple-700 transition-all duration-200 shadow-md hover:shadow-lg dark:bg-purple-700 dark:hover:bg-purple-800">
    <i class="fab fa-github mr-2" aria-hidden="true"></i>See more experiments on GitHub <span class="ml-1">→</span>
  </a>
</div>