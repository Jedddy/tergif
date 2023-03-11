import os
import cv2
from time import sleep

from PIL import Image


class ImgToAscii:
    """An Image converter class,

    Converts image to ascii characters"""
    def __init__(self, image: Image.Image, size: int = 50):
        self.img = image
        # ASCII chars used for brightness scale. You can change this if you want. 
        # self.ascii_chars = [' ', ' ', '*', '*', '/', '/', '^','$', '$', '#', '#']
        self.ascii_chars = ['  ', '  ',  '--',  '--', '~~', '~~', '++', '++', '==', '==', '==']
        self.base_width = size

    def convert_img(self, image: Image.Image) -> Image.Image: 
        aspect_ratio = image.size[0] / image.size[1]
        height = aspect_ratio * self.base_width
        img = image.resize((int(self.base_width), int(height)))
        return img.convert(mode="L")

    def process_img(self) -> str:
        # Opens image and converts to RGBA so images without background would work.
        im = self.convert_img(self.img.convert("RGBA"))
        pixl = im.getdata()

        newpix = [self.ascii_chars[pix//25] for pix in pixl]
        text = ''
        count = 0

        for i in newpix:
            text += i
            count += 1

            if count == self.base_width:
                text += '\n'
                count = 0

        return text + "Press CTRL + C to exit."


def player(gif_path: str):
    os.system('cls')
    cam = cv2.VideoCapture(f'gifs/{gif_path}')
    fps = cam.get(cv2.CAP_PROP_FPS)

    try:
        while True:
            check, frm = cam.read()

            if check:
                img = ImgToAscii(Image.fromarray(frm))
                print(img.process_img(), end="\r")
                sleep(fps/(fps*60))  # This is bs I HAVE NO IDEA WHAT TO DO HERE fk framerates
            else: 
                cam = cv2.VideoCapture(f'gifs/{gif_path}')

    except KeyboardInterrupt:
        os.system("cls" if os.name == "nt" else "clear")
        print("Quitting...")
        cam.release()
        cv2.destroyAllWindows()
