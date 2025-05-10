---
title: Images
layout: home
parent: Game Engine
permalink: /game-engine/images
---

# Images

## CIF - Compressed Image File

Dark Earth uses a 8-bit image format containing 256 colours and a 640 by 480 screen resolution. Each image has their own optimised palette and using dithering to reduce the image size. The images are compressed with Lempel-Ziv-Welch (LZW) compression algorithm.

### File Format

* **Header**: 0x10 bytes
    * **version**: 0x01 (4 bytes)
    * **unknown**: - (4 bytes)
    * **Width**: 640 (4 bytes)
    * **Height**: 480 (4 bytes)
* **Palette**: 256 * 3 bytes (RGB) = 0x300 bytes
* **Compressed Image Data**: (File Size - 0x310) bytes

<a href="{{ site.baseurl }}/assets/game/datas/l01/IMAGES/FL01C6L0.png" style="margin: 6px; display: inline-flex; border-radius: 15px; border: 1px solid #80808042; padding: 5px;">
    <img src="{{ site.baseurl }}/assets/game/datas/l01/IMAGES/FL01C6L0.png" alt="Sound" style="border-radius: 10px" />
</a>

## FLC - Animation File
FLC is a file format used for storing animation data. It is a compressed format that can store multiple frames of animation in a single file. FLC data is bundle inside .CJR files.

### File Format
TODO
