---
title: Cutscenes
layout: home
parent: Gallery
nav_order: 4
permalink: /gallery/cutscenes
images:
- image_path: assets/images/cutscenes/CUTSCE01.png
  title: Cutscene 01
  link: assets/images/cutscenes/CUTSCE01.png
- image_path: assets/images/cutscenes/CUTSCE02.png
  title: Cutscene 02
  link: assets/images/cutscenes/CUTSCE02.png
- image_path: assets/images/cutscenes/CUTSCE03.png
  title: Cutscene 03
  link: assets/images/cutscenes/CUTSCE03.png
- image_path: assets/images/cutscenes/CUTSCE04.png
  title: Cutscene 04
  link: assets/images/cutscenes/CUTSCE04.png
- image_path: assets/images/cutscenes/CUTSCE05.png
  title: Cutscene 05
  link: assets/images/cutscenes/CUTSCE05.png
- image_path: assets/images/cutscenes/CUTSCE06.png
  title: Cutscene 06
  link: assets/images/cutscenes/CUTSCE06.png
- image_path: assets/images/cutscenes/CUTSCE07.png
  title: Cutscene 07
  link: assets/images/cutscenes/CUTSCE07.png
- image_path: assets/images/cutscenes/CUTSCE08.png
  title: Cutscene 08
  link: assets/images/cutscenes/CUTSCE08.png
- image_path: assets/images/cutscenes/CUTSCE09.png
  title: Cutscene 09
  link: assets/images/cutscenes/CUTSCE09.png
- image_path: assets/images/cutscenes/CUTSCE10.png
  title: Cutscene 10
  link: assets/images/cutscenes/CUTSCE10.png
- image_path: assets/images/cutscenes/CUTSCE11.png
  title: Cutscene 11
  link: assets/images/cutscenes/CUTSCE11.png
- image_path: assets/images/cutscenes/CUTSCE12.png
  title: Cutscene 12
  link: assets/images/cutscenes/CUTSCE12.png
- image_path: assets/images/cutscenes/CUTSCE13.png
  title: Cutscene 13
  link: assets/images/cutscenes/CUTSCE13.png
- image_path: assets/images/cutscenes/CUTSCE14.png
  title: Cutscene 14
  link: assets/images/cutscenes/CUTSCE14.png
- image_path: assets/images/cutscenes/CUTSCE15.png
  title: Cutscene 15
  link: assets/images/cutscenes/CUTSCE15.png
- image_path: assets/images/cutscenes/CUTSCE16.png
  title: Cutscene 16
  link: assets/images/cutscenes/CUTSCE16.png
- image_path: assets/images/cutscenes/CUTSCE17.png
  title: Cutscene 17
  link: assets/images/cutscenes/CUTSCE17.png
- image_path: assets/images/cutscenes/CUTSCE18.png
  title: Cutscene 18
  link: assets/images/cutscenes/CUTSCE18.png
- image_path: assets/images/cutscenes/CUTSCE19.png
  title: Cutscene 19
  link: assets/images/cutscenes/CUTSCE19.png
- image_path: assets/images/cutscenes/CUTSCE20.png
  title: Cutscene 20
  link: assets/images/cutscenes/CUTSCE20.png
- image_path: assets/images/cutscenes/CUTSCE21.png
  title: Cutscene 21
  link: assets/images/cutscenes/CUTSCE21.png
- image_path: assets/images/cutscenes/CUTSCE22.png
  title: Cutscene 22
  link: assets/images/cutscenes/CUTSCE22.png
---

# Cutscenes

<div>
    {% for image in page.images %}
        <a href="{{ site.baseurl }}/{{ image.link }}" style="margin: 6px; display: inline-flex; border-radius: 15px; border: 1px solid #80808042; padding: 5px;">
            <img src="{{ site.baseurl }}/{{ image.image_path }}" alt="{{ image.title}}" style="border-radius: 10px" />
        </a>
    {% endfor %}
</div>
