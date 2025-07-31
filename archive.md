---
layout: page
title: Archive
permalink: /archive/
---

# Blog Archive

Browse all posts in the CAIO Playbook series, organized by date and category.

## All Posts

{% for post in site.posts %}
  {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
  {% capture nyear %}{{ post.next.date | date: '%Y' }}{% endcapture %}
  
  {% if year != nyear %}
### {{ year }}
  {% endif %}

- **{{ post.date | date: "%B %d" }}** - [{{ post.title }}]({{ post.url | relative_url }})
  {%- if post.categories.size > 0 -%}
  <br><small>Categories: {{ post.categories | join: ", " }}</small>
  {%- endif -%}
{% endfor %}

## By Category

{% assign categories = site.posts | map: 'categories' | join: ',' | split: ',' | uniq | sort %}

{% for category in categories %}
### {{ category | capitalize }}

{% for post in site.posts %}
  {% if post.categories contains category %}
- [{{ post.title }}]({{ post.url | relative_url }}) - {{ post.date | date: "%B %d, %Y" }}
  {% endif %}
{% endfor %}
{% endfor %}

## By Tag

{% assign tags = site.posts | map: 'tags' | join: ',' | split: ',' | uniq | sort %}

<div class="tag-cloud">
{% for tag in tags %}
  <span class="tag">{{ tag }}</span>
{% endfor %}
</div>

---

*Can't find what you're looking for? Use your browser's search function (Ctrl+F or Cmd+F) to search this page.*