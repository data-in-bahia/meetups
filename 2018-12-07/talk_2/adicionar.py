from PIL import Image


rosto = Image.open("rosto.png")

import os, subprocess
from os.path import join

outputdir = 'saida'

inputdir = 'raw'

for i, file_path in enumerate(os.listdir('raw')):

    im1 = Image.open(join(inputdir, file_path))

    im1.paste(rosto, (20, 20))

    im1.save(join(outputdir, f"{i}.jpg"))
    print(f"data_negao/img/{i}.jpg")