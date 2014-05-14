#!/usr/bin/env python

import sys
import Image
sys.path.append("../3_task")
from itertools import product
from Turtle    import Turtle


def star():

    step  = 20
    side  = 250
    shift = side + 1j*side
    draw  = Turtle("star")

    for x, y in product([1, -1], [1, -1]):
        for i in xrange(0, side + 1, step):
            a = x*i             + shift
            b = y*1j*(side - i) + shift
            draw.addLine(a, b)

    draw.dumpImage()


def colourSquare():

    img    = Image.new( 'RGB', (255,255), "black")
    pixels = img.load()

    for i in xrange(img.size[0]):  
        for j in xrange(img.size[1]):
            pixels[i,j] = (i, 0, j) 
    img.save("img/colourSquare.png")


if __name__ == '__main__':

    star()
    colourSquare()