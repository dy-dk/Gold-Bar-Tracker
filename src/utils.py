import os
import sys
from PIL import Image, ImageTk

def image_search(img, raid: str = "") -> str:
    if getattr(sys, 'frozen', False):
        filepath = os.path.dirname(sys.executable)
    elif __file__:
        filepath, filename = os.path.split(os.path.realpath(__file__))

    return os.path.join(filepath, "img", img) if raid == "" else os.path.join(filepath, "img", raid, img)

def file_search(file):
    if getattr(sys, 'frozen', False):
        filepath = os.path.dirname(sys.executable)
    elif __file__:
        filepath, filename = os.path.split(os.path.realpath(__file__))
    return os.path.join(filepath,file)

def resize_image(img, newWidth, newHeight):
    pilImage = ImageTk.getimage(img).convert("RGBA")
    oldWidth, oldHeight = pilImage.size
    newImg = pilImage.resize((newWidth, newHeight), Image.LANCZOS)
    newPhotoImage = ImageTk.PhotoImage(newImg)
    return newPhotoImage