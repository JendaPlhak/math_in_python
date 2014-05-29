#! usr/bin/env python
import sys
sys.path.append('../2_task')

from PIL              import Image
from pascals_triangle import different_colors

import numpy as np

import cmath
import itertools


def newton_fractal(filename='', pol=[]):

    im     = Image.new("RGB", (1000, 1000), (255, 255, 255))
    colors = different_colors(3)


    roots = { 1 : 1,
              2 : -0.5 + 3**0.5 / 2 * 1j, 
              3 : -0.5 - 3**0.5 / 2 * 1j }

    for x, y in itertools.product(xrange(-500, 500), xrange(-500, 500)):
        z_n = x +  y * 1j
        for i in xrange(50):
            if 3 * z_n**2 == 0:
                break
            z_n = z_n - (z_n**3 - 1) / (3 * z_n**2)

        x += 500
        y += 500
        if abs(z_n - roots[1]) < 0.0001:
            im.putpixel((x, y), colors[0])
        elif abs(z_n - roots[2]) < 0.0001:
            im.putpixel((x, y), colors[1])
        elif abs(z_n - roots[3]) < 0.0001:
            im.putpixel((x, y), colors[2])
        else:
            im.putpixel((x, y), (0, 0, 0))

    if filename:
        im.save('img/'+ filename +'.png')
    else:
        im.show()


def mandelbrots_set(filename=''):

    im     = Image.new("RGB", (1000, 1000), (255, 255, 255))
    #colors = different_colors(2)
    for x, y in itertools.product(xrange(-500, 500), xrange(-500, 500)):
        C   = x * 0.01 + y * 1j * 0.01
        z_n = 0
        for i in xrange(30):
            if abs(z_n) > 2:
                break
            z_n = z_n**2 + C

        if abs(z_n) < 2:
            col = tuple(3 * [0])
        else:
            col = tuple(3 * [255])

        im.putpixel((x + 500, y + 500), col)

    if filename:
        im.save('img/'+ filename +'.png')
    else:
        im.show()


def julia_set(C, filename=''):

    im = Image.new("RGB", (400, 400), (255, 255, 255))

    for x, y in itertools.product(xrange(-200, 200), xrange(-200, 200)):
        z_n = x * 0.01 + y * 1j*0.01
        #print z_n
        for i in range(30):
            if abs(z_n) > 2:
                break
            z_n = z_n**2 + C
        #print "complex number: {}".format(z_n)
        #print "absolute value: {}".format(abs(z_n))

        if abs(z_n) < 2:
            #print "=======> Hooray"
            col = tuple( 3 * [0])
        else:
            col = tuple( 3 * [255])
    
        im.putpixel((x + 200, y + 200), col)

    if filename:
        im.save('img/'+ filename +'.png')
    else:
        im.show()   

if __name__ == '__main__':

    #fractal('newton_fractal')
    #mandelbrots_set('mandelbrots_set')
    #C = -0.13 + 0.75j
    #julia_set(C, filename='julia_set')
    
    p = [1,0,0,-1]

    print roots(p)