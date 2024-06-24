---
layout: default
permalink: /appearances/
title: "Appearances"
---

<section class="grid grid-cols-1 gap-8 w-full">
  <h1 class="font-semibold text-4xl">Appearances</h1>
  <table class="table-auto border-collapse border border-slate-500">
    <thead>
        <tr class="*:text-left *:p-2">
            <th class="border border-slate-600">Date</th>
            <th class="border border-slate-600">Type</th>
            <th class="border border-slate-600">Title</th>
        </tr>
    </thead>
    <tbody>
    {% assign sorted_appearances = site.appearances | sort: 'date' | reverse %}
    {% for appearance in sorted_appearances %}
      <tr class="*:p-2">
        <td class="border border-slate-600">{{ appearance.date | date:"%Y, %B %e" }}</td>
        <td class="border border-slate-600">{{ appearance.type }}</td>
        <td class="border border-slate-600">
            <a href="{{ appearance.link }}" class="no-underline">
                {{ appearance.title }}
            </a>
        </td>
      </tr>
    {% endfor %}
    </tbody>
  </table>
</section>
