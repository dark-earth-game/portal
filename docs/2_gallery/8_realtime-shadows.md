---
title: Realtime Shadows
layout: home
parent: Gallery
nav_order: 8
permalink: /gallery/realtime-shadows
images:
- image_path: assets/images/realtime-shadows/SHADOWS1.jpg
  title: Realtime Shadows Example
  link: assets/images/realtime-shadows/SHADOWS1.jpg
---

# Realtime Shadows

<div>
    {% for image in page.images %}
        <a href="{{ site.baseurl }}/{{ image.link }}" style="margin: 6px; display: inline-flex; border-radius: 15px; border: 1px solid #80808042; padding: 5px;">
            <img src="{{ site.baseurl }}/{{ image.image_path }}" alt="{{ image.title}}" style="border-radius: 10px" />
        </a>
    {% endfor %}
</div>
