---
title: Light Sourcing
layout: home
parent: Gallery
nav_order: 9
permalink: /gallery/lightsourcing
images:
- image_path: assets/images/lightsourcing/LIGHTS1.png
  title: Light Sourcing Example 1
  link: assets/images/lightsourcing/LIGHTS1.png
- image_path: assets/images/lightsourcing/LIGHTS2.png
  title: Light Sourcing Example 2
  link: assets/images/lightsourcing/LIGHTS2.png
- image_path: assets/images/lightsourcing/LIGHTS3.png
  title: Light Sourcing Example 3
  link: assets/images/lightsourcing/LIGHTS3.png
- image_path: assets/images/lightsourcing/LIGHTS4.png
  title: Light Sourcing Example 4
  link: assets/images/lightsourcing/LIGHTS4.png
---

# Light Sourcing

<div>
    {% for image in page.images %}
        <a href="{{ site.baseurl }}/{{ image.link }}" style="margin: 6px; display: inline-flex; border-radius: 15px; border: 1px solid #80808042; padding: 5px;">
            <img src="{{ site.baseurl }}/{{ image.image_path }}" alt="{{ image.title}}" style="border-radius: 10px" />
        </a>
    {% endfor %}
</div>
