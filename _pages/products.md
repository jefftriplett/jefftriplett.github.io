---
layout: default
title: "🛍️ Consuming: Products"
permalink: /products/
---

<section class="grid grid-cols-1 gap-8 w-full">
  <h1 class="font-semibold text-4xl">🛍️ Consuming: Products</h1>
  <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">
    {% assign sorted_products = site.products | sort: 'date' | reverse %}
    {% for product in sorted_products %}
      <article>
        <a href="{{ product.link }}" class="no-underline">
          <figure class="flex flex-col gap-4">
            {% if product.cover %}
              <img class="rounded-md transition ease-in-out delay-150 hover:-translate-y-1 hover:scale-110 duration-300" src="{{ product.cover }}" alt="Cover image for {{ product.title }}">
            {% endif %}
            <figcaption class="font-semibold text-center">{{ product.title }}</figcaption>
          </figure>
        </a>
      </article>
    {% endfor %}
  </div>
</section>
