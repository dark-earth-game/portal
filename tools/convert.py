import os
from PIL import Image

for filename in os.listdir('.'):
    if filename.endswith('.tif') or filename.endswith('.TIF'):
        im = Image.open(os.path.join(tiff_dir, filename))
        im.save(os.path.splitext(filename)[0] + f'.png')
