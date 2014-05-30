#! usr/bin/env python
import sys
sys.path.append('../2_task')

from PIL              import Image
from pascals_triangle import different_colors

import numpy as np

import cmath
import itertools
import colorsys


def newton_fractal(filename='', pol=[1,0,0,-1], frame=[-500, -500, 1000]):

    x0 = frame[0]
    y0 = frame[1]
    dt = frame[2]

    im     = Image.new("RGB", (1000, 1000), (255, 255, 255))
    roots  = np.roots( pol )
    colors = different_colors( len(roots) )

    for s, t in itertools.product(xrange(1000), xrange(1000)):
        z = x0 + s * dt / 1000. + (y0 + t * dt / 1000.) * 1j
        for i in xrange(50):
            if np.polyval( pol, z ) == 0 or np.polyval( np.polyder( pol ), z) == 0:
                break
            z = z - np.polyval( pol, z) / np.polyval( np.polyder( pol ), z)

        col = (0,0,0)
        for i, root in enumerate(roots):
            if abs(z - root) < 0.0001:
                col = colors[ i ]
        im.putpixel((s, t), col)

    if filename:
        im.save('img/'+ filename +'.png')
    else:
        im.show()


def mandelbrot_set(C=-0.13 + 0.75j, filename='', julia=False, frame=[-2,-2,3]):

    x0 = frame[0]
    y0 = frame[1]
    dt = frame[2]

    im = Image.new("RGB", (1000, 1000), (255, 255, 255))
    colors = different_colors(31)
    for s, t in itertools.product(xrange(1000), xrange(1000)):
        steps = 0
        if julia:
            z = x0 + s * dt / 1000. + (y0 + t * dt / 1000.) * 1j
        else:
            C = x0 + s * dt / 1000. + (y0 + t * dt / 1000.) * 1j
            z = 0

        for i in xrange(30):
            if abs(z) > 2:
                break
            z      = z**2 + C
            steps += 1

        #HSV_tuples = [(z.real * 1.0 /  31, 1, 0.85) for x in range(31) ]
        #RGB_tuples = map(lambda x: colorsys.hsv_to_rgb( *x ), HSV_tuples)
        #RGB_tuples = map(lambda x: tuple(map(lambda y: int(y * 255),x)),RGB_tuples)

        #if abs(z) < 2:
        #col = tuple( map( lambda x: int(x), [255 * z.real, 255*z.imag, 255*(z.real + z.imag)]))
        #col = tuple( map( lambda x: int(x), [255 * z.real, 255*z.imag, 255*(steps)]))
        col = colors[steps]
#        else:
            #col = tuple(3 * [255])

        im.putpixel((s, t), col)

    if filename:
        im.save('img/'+ filename +'.png')
    else:
        im.show()


if __name__ == '__main__':

    #newton_fractal(filename='newton_fractal', pol=[2,3,5,7,11])
    mandelbrot_set(filename='mandelbrot_steps')