#!/usr/bin/env python

from PIL import Image as pillow
from colors import EnumColor
import hashlib, os

class Image(object):
    def __init__(self, file):
        self.checksum = self.md5(file);
        self.image = self.load_image(file)
        self.width, self.height = self.image.size
        self.pix = self.image.load()

    def load_image(self, file):

        if (os.path.isfile(os.getcwd() + '/img/.cache/' + self.checksum + '.jpg')):
            print self.checksum
        if (os.path.isfile(file)):
            print 'generatin Temp image for ' + os.getcwd() + '/img/.cache/' + self.checksum + '.jpg'
            new_image = self.convert_pixels(pillow.open(file).convert('RGB'))
            self.save_image(new_image, 'img/.cache/' + self.checksum + '.jpg')

        return pillow.open(file).convert('RGB')

    def md5(self,fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    #refUrl: https://www.codementor.io/isaib.cicourel/image-manipulation-in-python-du1089j1u

    def save_image(self, image, path):
        image.save(path, 'jpeg')

    # Create a new image with the given size
    def create_image(self,i, j):
        image = pillow.new("RGB", (i, j), "white")
        return image

    def get_pixel(self,image, i, j):
        # Inside image bounds?
        width, height = image.size
        if i > width or j > height:
            return None

        pixel = image.getpixel((i, j))
        return pixel

    def convert_pixels(self, image):
        width, height = image.size

        new = self.create_image(width, height)
        pixels = new.load()

        for i in range(width):
            for j in range(height):
                pixel = self.get_pixel(image, i, j)
                new_color = EnumColor.rgb(pixel, True, True)
                pixels[i, j] = (int(new_color.rgb[0]), int(new_color.rgb[1]), int(new_color.rgb[2]))

        return new