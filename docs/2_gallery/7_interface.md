---
title: Interface
layout: home
parent: Gallery
nav_order: 7
permalink: /gallery/interface
images:
- image_path: assets/images/interface/DETAILS.png
  title: Details Screen
  link: assets/images/interface/DETAILS.png
- image_path: assets/images/interface/DIALOG.png
  title: Dialog Interface
  link: assets/images/interface/DIALOG.png
- image_path: assets/images/interface/INVENT.png
  title: Inventory Interface
  link: assets/images/interface/INVENT.png
- image_path: assets/images/interface/LOAD.png
  title: Load Game Screen
  link: assets/images/interface/LOAD.png
- image_path: assets/images/interface/MAINMENU.png
  title: Main Menu
  link: assets/images/interface/MAINMENU.png
- image_path: assets/images/interface/SAVE.png
  title: Save Game Screen
  link: assets/images/interface/SAVE.png
- image_path: assets/images/interface/SOUND.png
  title: Sound Options
  link: assets/images/interface/SOUND.png
---

# Interface

<div>
    {% for image in page.images %}
        <a href="{{ site.baseurl }}/{{ image.link }}" style="margin: 6px; display: inline-flex; border-radius: 15px; border: 1px solid #80808042; padding: 5px;">
            <img src="{{ site.baseurl }}/{{ image.image_path }}" alt="{{ image.title}}" style="border-radius: 10px" />
        </a>
    {% endfor %}
</div>
