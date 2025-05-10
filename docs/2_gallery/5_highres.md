---
title: High Resolution
layout: home
parent: Gallery
nav_order: 5
permalink: /gallery/highres
images:
- image_path: assets/images/cutscenes/HIGHRES.png
  title: High Resolution
  link: assets/images/cutscenes/HIGHRES.png
- image_path: assets/images/cutscenes/PERSO.png
  title: Characters
  link: assets/images/cutscenes/PERSO.png
- image_path: assets/images/highres/Arkhan.png
  title: Arkhan (High Resolution)
  link: assets/images/highres/Arkhan.png
- image_path: assets/images/highres/Thananda.png
  title: Thananda (High Resolution)
  link: assets/images/highres/Thananda.png
- image_path: assets/images/highres/DarkEart.png
  title: Dark Earth (High Resolution)
  link: assets/images/highres/DarkEart.png
- image_path: assets/images/renders/arkhan.png
  title: Arkhan Render
  link: assets/images/renders/arkhan.png
- image_path: assets/images/images/HIGHRES.png
  title: High Resolution
  link: assets/images/images/HIGHRES.png
---

# High Resolution Images

<div>
    {% for image in page.images %}
        <a href="{{ site.baseurl }}/{{ image.link }}" style="margin: 6px; display: inline-flex; border-radius: 15px; border: 1px solid #80808042; padding: 5px;">
            <img src="{{ site.baseurl }}/{{ image.image_path }}" alt="{{ image.title}}" style="border-radius: 10px" />
        </a>
    {% endfor %}
</div>
