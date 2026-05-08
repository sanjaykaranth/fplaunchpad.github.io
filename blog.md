---
layout: blog-listing
title: Blog
permalink: /blog/
---

<p class="rss-subscribe">Subscribe via <a href="{{ '/feed.xml' | relative_url }}">RSS feed</a></p>

{% assign blog_posts = site.blog | sort: 'date' | reverse %}
{% if blog_posts.size == 0 %}
<p style="color: #828282;">No posts yet — check back soon.</p>
{% else %}
{% for post in blog_posts %}
<article class="blog-preview">
  <h2 class="blog-preview-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <p class="post-meta">{{ post.date | date: "%-d %B %Y" }}{% if post.author %} · {{ post.author }}{% endif %}</p>
  <p class="blog-preview-excerpt">{{ post.excerpt | strip_html | truncatewords: 50 }}</p>
  <a class="blog-preview-link" href="{{ post.url | relative_url }}">Read more →</a>
</article>
{% endfor %}
{% endif %}
