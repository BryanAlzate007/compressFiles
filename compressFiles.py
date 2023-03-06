#nuevo proyecto compresor de archivos
from PIL import Image
import os

folder = "/home/bryan/Documents/Images/"
if __name__ == "__main__":
    for filename in os.listdir(folder):
        name, extension = os.path.splitext(folder + filename)

        if extension in [".jpg",".jpeg",".png"]:
            picture = Image.open(folder + filename)
            picture.save (folder + "compressed_"+filename, optimize=True, quality=60)