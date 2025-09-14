---
layout: soul
title: Soul
permalink: /soul/
---

<section id="soul">
  <h2>Do you know what that means??</h2>

  <ul class="blog-list">
    {% for post in site.posts %}
      <li class="blog-item">
        <a href="{{ post.url | relative_url }}" class="blog-link">
          {{post.title}}
        </a>
        <span class="blog-date">{{ post.date | date: "%B %d, %Y" }}</span>
      </li>
      <br><br> <!-- Extra space between posts -->
    {% endfor %}
  </ul>
</section>

```html

```
