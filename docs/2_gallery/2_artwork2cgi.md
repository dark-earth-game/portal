---
title: Artwork to CGI
layout: home
parent: Gallery
nav_order: 2
permalink: /gallery/artwork2cgi
images:
- image_path: assets/images/artwork2cgi/BOUGE.png
  title: Dark Earth Artwork to CGI - BOUGE
  link: assets/images/artwork2cgi/BOUGE.png
- image_path: assets/images/artwork2cgi/BOUGE.GIF
  title: Dark Earth Artwork to CGI - BOUGE (GIF)
  link: assets/images/artwork2cgi/BOUGE.GIF
- image_path: assets/images/artwork2cgi/CHAMBRE.png
  title: Dark Earth Artwork to CGI - CHAMBRE
  link: assets/images/artwork2cgi/CHAMBRE.png
- image_path: assets/images/artwork2cgi/CHAMBRE.GIF
  title: Dark Earth Artwork to CGI - CHAMBRE (GIF)
  link: assets/images/artwork2cgi/CHAMBRE.GIF
- image_path: assets/images/artwork2cgi/HOSPI.png
  title: Dark Earth Artwork to CGI - HOSPI
  link: assets/images/artwork2cgi/HOSPI.png
- image_path: assets/images/artwork2cgi/HOSPI.GIF
  title: Dark Earth Artwork to CGI - HOSPI (GIF)
  link: assets/images/artwork2cgi/HOSPI.GIF
- image_path: assets/images/artwork2cgi/PIPEAU.png
  title: Dark Earth Artwork to CGI - PIPEAU
  link: assets/images/artwork2cgi/PIPEAU.png
- image_path: assets/images/artwork2cgi/PIPEAU.GIF
  title: Dark Earth Artwork to CGI - PIPEAU (GIF)
  link: assets/images/artwork2cgi/PIPEAU.GIF
---

# Artwork to CGI

<div>
    {% for image in page.images %}
        <a href="{{ site.baseurl }}/{{ image.link }}" style="margin: 6px; display: inline-flex; border-radius: 15px; border: 1px solid #80808042; padding: 5px;">
            <img src="{{ site.baseurl }}/{{ image.image_path }}" alt="{{ image.title}}" style="border-radius: 10px" />
        </a>
    {% endfor %}
</div>
