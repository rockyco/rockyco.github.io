---
layout: page
title: Blog
permalink: /blog/
---

Notes on turning algorithms into trustworthy hardware.

<div class="cards">
{% assign posts = site.posts | where: "lang", "en" %}
{% for post in posts %}
  <div class="card">
    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <p>{{ post.excerpt | strip_html | truncate: 200 }}</p>
    <p class="meta">{{ post.date | date: "%B %-d, %Y" }}
      {% assign zh = site.posts | where: "translation_id", post.translation_id | where_exp: "p", "p.lang == 'zh'" | first %}
      {% if zh %}<span class="dot">&middot;</span><a href="{{ zh.url | relative_url }}">中文</a>{% endif %}
    </p>
  </div>
{% endfor %}
</div>
