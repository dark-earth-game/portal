---
title: Promotional Art
layout: home
parent: Gallery
nav_order: 12
permalink: /gallery/promotional_art
images:
- image_path: assets/images/promotional_art/IMG_5950.jpg
  title: Promotional Art 1
  link: assets/images/promotional_art/IMG_5950.jpg
- image_path: assets/images/promotional_art/IMG_5952.jpg
  title: Promotional Art 2
  link: assets/images/promotional_art/IMG_5952.jpg
- image_path: assets/images/promotional_art/IMG_5953.JPG
  title: Promotional Art 3
  link: assets/images/promotional_art/IMG_5953.JPG
- image_path: assets/images/promotional_art/IMG_5954.JPG
  title: Promotional Art 4
  link: assets/images/promotional_art/IMG_5954.JPG
---

# Promotional Art

<div>
    {% for image in page.images %}
        <a href="{{ site.baseurl }}/{{ image.link }}" style="margin: 6px; display: inline-flex; border-radius: 15px; border: 1px solid #80808042; padding: 5px;">
            <img src="{{ site.baseurl }}/{{ image.image_path }}" alt="{{ image.title}}" style="border-radius: 10px" />
        </a>
    {% endfor %}
</div>
