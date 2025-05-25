---
layout: default
title: "🎮 Playing: Games"
permalink: /games/
---

<section class="grid grid-cols-1 gap-8 w-full">
  <h1 class="font-semibold text-4xl">🎮 Playing: Games</h1>
  <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">
    {% assign sorted_games = site.games | sort: 'date' | reverse %}
    {% for game in sorted_games %}
      <article>
        <a href="{{ game.link }}" class="no-underline">
          <figure class="flex flex-col gap-2 sm:gap-4 min-h-80">
            {% if game.cover %}
              <img class="rounded-md transition ease-in-out delay-150 hover:-translate-y-1 hover:scale-110 duration-300" src="{{ game.cover }}" alt="Cover image for {{ game.title }}">
            {% endif %}
            <figcaption class="font-semibold text-center">{{ game.title }}</figcaption>
          </figure>
        </a>
      </article>
    {% endfor %}
  </div>
</section>
