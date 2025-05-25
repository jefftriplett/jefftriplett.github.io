---
layout: default
title: "📺 Watching: Movies"
permalink: /movies/
---

<section class="grid grid-cols-1 gap-8 w-full">
  <h1 class="font-semibold text-4xl">📺 Watching: Movies</h1>
  <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">
    {% assign sorted_movies = site.movies | sort: 'date' | reverse %}
    {% for movie in sorted_movies %}
      <article>
        <a href="{{ movie.link }}" class="no-underline">
          <figure class="flex flex-col gap-2 sm:gap-4 min-h-80">
            {% if movie.cover %}
              <img class="rounded-md transition ease-in-out delay-150 hover:-translate-y-1 hover:scale-110 duration-300" src="{{ movie.cover }}" alt="Cover image for {{ movie.title }}">
            {% endif %}
            <figcaption class="font-semibold text-center">{{ movie.title }}</figcaption>
          </figure>
        </a>
      </article>
    {% endfor %}
  </div>
</section>
