---
layout: default
title: "📺 Watching: Series"
permalink: /series/
---

<section class="grid grid-cols-1 gap-8 w-full">
  <h1 class="font-semibold text-4xl">📺 Watching: Series</h1>
  <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">
    {% assign sorted_series = site.series | sort: 'date' | reverse %}
    {% for series in sorted_series %}
      <article>
        <a href="{{ series.link }}" class="no-underline">
          <figure class="flex flex-col gap-2 sm:gap-4 h-full">
            {% if series.cover %}
              <div class="aspect-[2/3] overflow-hidden rounded-md">
                <img class="w-full h-full object-cover transition duration-300 ease-in-out hover:scale-110" src="{{ series.cover }}" alt="Cover image for {{ series.title }}">
              </div>
            {% endif %}
            <figcaption class="text-sm sm:text-base font-semibold text-center">{{ series.title }}</figcaption>
          </figure>
        </a>
      </article>
    {% endfor %}
  </div>
</section>
