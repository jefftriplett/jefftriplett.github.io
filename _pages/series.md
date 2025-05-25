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
          <figure class="flex flex-col gap-2 sm:gap-4 min-h-80">
            {% if series.cover %}
              <img class="rounded-md transition ease-in-out delay-150 hover:-translate-y-1 hover:scale-110 duration-300" src="{{ series.cover }}" alt="Cover image for {{ series.title }}">
            {% endif %}
            <figcaption class="font-semibold text-center">{{ series.title }}</figcaption>
          </figure>
        </a>
      </article>
    {% endfor %}
  </div>
</section>
