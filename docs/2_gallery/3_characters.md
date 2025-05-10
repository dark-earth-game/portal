---
title: In-Game Characters
layout: home
parent: Gallery
nav_order: 3
permalink: /gallery/characters
images:
- image_path: assets/images/characters/ARKHAN.png
  title: Arkhan
  link: assets/images/characters/ARKHAN.png
- image_path: assets/images/characters/ARMAL.png
  title: Armal
  link: assets/images/characters/ARMAL.png
- image_path: assets/images/characters/ARMAL2.png
  title: Armal (Alternate)
  link: assets/images/characters/ARMAL2.png
- image_path: assets/images/characters/LODHAR.png
  title: Lodhar
  link: assets/images/characters/LODHAR.png
- image_path: assets/images/characters/PHEDORI2.png
  title: Phedoria (Alternate)
  link: assets/images/characters/PHEDORI2.png
- image_path: assets/images/characters/PHEDORIA.png
  title: Phedoria
  link: assets/images/characters/PHEDORIA.png
- image_path: assets/images/characters/RHYLSADA.png
  title: Rhylsada
  link: assets/images/characters/RHYLSADA.png
- image_path: assets/images/characters/ZED.png
  title: Zed
  link: assets/images/characters/ZED.png
---

# Characters

<div>
    {% for image in page.images %}
        <a href="{{ site.baseurl }}/{{ image.link }}" style="margin: 6px; display: inline-flex; border-radius: 15px; border: 1px solid #80808042; padding: 5px;">
            <img src="{{ site.baseurl }}/{{ image.image_path }}" alt="{{ image.title}}" style="border-radius: 10px" />
        </a>
    {% endfor %}
</div>
