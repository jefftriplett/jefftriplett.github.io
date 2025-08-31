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
          <figure class="flex flex-col gap-2 sm:gap-4 h-full">
            {% if product.cover %}
              <div class="aspect-square overflow-hidden rounded-md">
                <img class="w-full h-full object-contain bg-white transition duration-300 ease-in-out hover:scale-110" src="{{ product.cover }}" alt="Cover image for {{ product.title }}">
              </div>
            {% endif %}
            <figcaption class="text-sm sm:text-base font-semibold text-center">{{ product.title }}</figcaption>
          </figure>
        </a>
      </article>
    {% endfor %}
  </div>
</section>
