---
title: Game Engine
layout: home
nav_order: 4
permalink: /game-engine
---

# Game Engine

<img src="{{ site.baseurl }}/assets/topbar/4_engine.jpg" alt="Dark Earth" style="display: inline-flex; border-radius: 15px; border: 1px solid #80808042; padding: 2px;" />

{: .no_toc }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Overview

Dark Earth uses pre-rendered backgrounds with 3D software rendered characters, a technique use in the early 90s due to hardware constraints. Alone in the Dark (AITD) was the pioneer of pre-rendered backgrounds and use static images that were hand drawn on top of wireframes of a 3D scene. Each image corresponding to a different camera view of the scene. Dark Earth followed the same approach and improved what AITD did by using a depth map, a light map and shadow map.

Dark Earth is devided into Levels or Scenes, where each scene has different camera angles and/or rooms. It uses a scene geometry mesh for collision detection and to allow the player to navigate in the 3d environment of the scene, using the depth map to correctily overlay the pre-renderer backgrouds.

Each scene has a dedicated scripting Dynamic Library (DLL) which contain the behaviour and interactions of the level.
