import matplotlib.pyplot as plt
import os
from PIL import Image

directory = "/Users/emanuel/Downloads/nutriu_10.12" # root - tu promijeni path u root folder gdje su ti slike

def remove_alpha(image,):
    color=(255, 255, 255)
    image.load()  # treba za split()
    background = Image.new('RGB', image.size, color)
    background.paste(image, mask=image.split()[3])  # 3 je alpha channel
    return background


def program(path):
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".png"):
                pic_path = directory+filename
                pic = Image.open(os.path.join(subdir, filename))
                if pic.mode in ('RGBA', 'LA') or (pic.mode == 'P' and 'transparency' in pic.info):
                    pic=remove_alpha(pic)
                    pic.save(os.path.join(subdir, filename))
                    print(os.path.join(subdir, filename))  
