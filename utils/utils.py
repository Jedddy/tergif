from PIL import Image
import os
import cv2
from time import sleep

class ImgToAscii:
    """An Image converter class,
    
    Converts image to ascii characters"""
    def __init__(self, img_name, size=None):
        self.img_name = img_name 
        # ASCII chars used for brightness scale. You can change this if you want. 
        # self.ascii_chars = [' ', ' ', '*', '*', '/', '/', '^','$', '$', '#', '#']
        self.ascii_chars = ['  ', '  ',  '--',  '--', '~~', '~~', '++', '++', '==', '==', '==']
        # Base width for resizing
        self.base_width = size


    # Resizes Image and converts to grayscale
    def convert_img(self, img): 
        self.aspect_ratio = img.size[0] / img.size[1]
        self.height = self.aspect_ratio * self.base_width
        self.img = img.resize((int(self.base_width), int(self.height)))
        return self.img.convert(mode="L")

    # Converts image to ASCII and saves it on a txt file.
    def process_img(self):
        # Opens image and converts to RGBA so images without background would work.
        with Image.open(self.img_name).convert("RGBA") as image:
            self.im = self.convert_img(image)
            self.pixl = self.im.getdata()

        self.newpix = [self.ascii_chars[pix//25] for pix in self.pixl]

        self.text = ''
        self.count = 0

        for i in self.newpix:
            self.text += i
            self.count += 1
            if self.count == self.base_width:
                self.text += '\n'
                self.count = 0
        
        with open('converted.txt', 'w') as self.txt:
            self.txt.write(self.text)
# End Class

def clear_folder():
    """Clears Folders"""
    try: 
        for i in os.listdir('frames'):
            os.remove('frames/' + i)
    except FileNotFoundError:
        pass

def player(gif_path):
    os.system('cls')
    num_frame = 0
    cam = cv2.VideoCapture(f'gifs/{gif_path}')
    
    while True:
        check, frm = cam.read()
        if check:
            cv2.imwrite(f'frames/{str(num_frame)}.jpg', frm)
            num_frame += 1
        else: 
            break
    cam.release()
    cv2.destroyAllWindows()

    try:
        i = 0
        lenght = len(os.listdir('frames'))
        while True:
            img = ImgToAscii(f"frames/{i}.jpg", size=50) # Edit the size to your liking.
            img.process_img()
            with open('converted.txt', 'r') as imgs:
                imgs = imgs.read()
                print(imgs + '\nPress CTRL + C to exit.', end='\r', flush=True)
                sleep(lenght/(lenght*30)) # Speed of the animation, lower == faster animation.
            i += 1
            if i == lenght:
                i = 0
    except KeyboardInterrupt:
        os.system('cls')
        t = lenght//20
        print(f'Terminating...\nPlease wait for {t} seconds.')
        sleep(t)
        clear_folder()
        print('Program done.')
    