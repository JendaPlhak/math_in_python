#!/usr/bin/env python
from PIL import Image


def round_1(path="img/hide_and_seek1_orig.png"):

    img    = Image.open(path)
    pixels = img.load()
    for x in xrange(img.size[0]):
        for y in xrange(img.size[1]):
            if pixels[x, y][2]:
                pixels[x, y] = (255,255,255 )
            else:
                pixels[x, y] = (0,0,0 )
    img.save("img/hide_and_seek1.png")
        

def round_2(path="img/hide_and_seek2_orig.png"):

    img_orig = Image.open(path)
    pixels   = img_orig.load()
    img      = Image.new('RGB', img_orig.size, 'white')
    for y in xrange(1, img.size[1]):
        for x in xrange(1, img.size[0]):
            if pixels[x, y][2] < pixels[x-1, y][2] or pixels[x, y][0] > pixels[x, y-1][0]:
                img.putpixel((x, y), (0,0,0))

    img.save("img/hide_and_seek2.png")


def round_3(path="img/hide_and_seek3_orig.png"):

    img     = Image.open(path)
    pixels  = img.load()
    shift   = img.size[1]/2
    img_new = Image.new('RGB', img.size, 'black')
    for x in xrange(img.size[0]):
        for y in xrange(img.size[1]/2):
            if bool(pixels[x, y][0]) != bool(pixels[x, y + shift][0]):
                img_new.putpixel([x, y], (255,255,255, 255))

    img.save("img/hide_and_seek3.png")


if __name__ == '__main__':

    round_1()
    round_2()
    round_3()