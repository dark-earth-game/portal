---
title: Logo
layout: home
parent: Gallery
nav_order: 13
permalink: /gallery/logo
images:
- image_path: assets/images/logo/KALISTO.JPG
  title: Kalisto Logo
  link: assets/images/logo/KALISTO.JPG
- image_path: assets/images/logo/LOGODKE.png
  title: Dark Earth Logo
  link: assets/images/logo/LOGODKE.png
---

# Logo

<div>
    {% for image in page.images %}
        <a href="{{ site.baseurl }}/{{ image.link }}" style="margin: 6px; display: inline-flex; border-radius: 15px; border: 1px solid #80808042; padding: 5px;">
            <img src="{{ site.baseurl }}/{{ image.image_path }}" alt="{{ image.title}}" style="border-radius: 10px" />
        </a>
    {% endfor %}
</div>
