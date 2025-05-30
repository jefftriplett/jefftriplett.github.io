---
layout: default
title: "🎵 Listening: Music"
permalink: /music/
sitemap: true
---

<div class="w-full">
  <div class="prose prose-a:underline prose-a:px-1 prose-a:py-1 sm:prose-md md:prose-lg lg:prose-lg xl:prose-xl dark:prose-invert">
    <h1 class="font-semibold text-4xl">🎵 Listening: Music</h1>
  </div>

  <div class="mt-8">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      {% assign sorted_collection = site.music | sort: 'date' | reverse %}
      {% for item in sorted_collection %}
        <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300">
          <div class="mb-2">
            <a href="{{ item.link }}" target="_blank" rel="noopener" class="text-lg font-semibold hover:text-blue-600 dark:hover:text-blue-400 transition-colors duration-300">{{ item.title }}</a>
          </div>
          <div class="text-sm text-gray-600 dark:text-gray-400 mb-3">
            {{ item.date | date: "%B %d, %Y" }}
          </div>
          {% if item.youtube_id %}
          <div class="mb-3">
            <div class="aspect-w-16 aspect-h-9">
              <iframe src="https://www.youtube.com/embed/{{ item.youtube_id }}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen class="w-full h-full rounded-md"></iframe>
            </div>
          </div>
          {% elsif item.spotify_id %}
          <div class="mb-3">
            <iframe src="https://open.spotify.com/embed/track/{{ item.spotify_id }}" width="100%" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media" class="rounded-md"></iframe>
          </div>
          {% elsif item.cover %}
          <div class="mb-3">
            <img src="{{ item.cover }}" alt="{{ item.title }}" class="w-full h-auto rounded-md">
          </div>
          {% endif %}
          {% if item.content != empty %}
          <div class="text-sm text-gray-700 dark:text-gray-300">
            {{ item.content }}
          </div>
          {% endif %}
          <div class="mt-2">
            <a href="{{ item.link }}" target="_blank" rel="noopener" class="text-blue-600 dark:text-blue-400 text-sm hover:underline">
              {% if item.youtube_id %}Watch{% else %}Listen{% endif %}
            </a>
          </div>
        </div>
      {% endfor %}
    </div>
  </div>
</div>
