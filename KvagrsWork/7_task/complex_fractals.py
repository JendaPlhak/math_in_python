#!/usr/bin/env python

import sys
sys.path.append('../2_task')

from PIL              import Image
from pascals_triangle import different_colors
from random           import random
from itertools        import product

import numpy as np

import cmath
import math
import colorsys



def newton_fractal(filename='', pol=[1,0,0,-1], frame=[-500, -500, 1000]):

    x0 = frame[0]
    y0 = frame[1]
    dt = frame[2]

    im     = Image.new("RGB", (250, 250), (255, 255, 255))
    roots  = np.roots( pol )
    colors = different_colors( len(roots) )
    print roots


    for s, t in product(xrange(250), xrange(250)):
        z = x0 + s * dt / 250. + (y0 + t * dt / 250.) * 1j
        for i in xrange(100):

            if z**3 == 0:            
                break

            z = z - z**3 / (3. * z**2)
            #print z
            #if np.polyval( pol, z ) == 0 or np.polyval( np.polyder( pol ), z) == 0:
            #    break
            #z = z - np.polyval( pol, z) / np.polyval( np.polyder( pol ), z)

        #print colors
        col = (0,0,0)
        for i, root in enumerate(roots):
            
            if abs(z - root) < 0.0001:
                print abs(z - root)
                col = colors[ i ]
            #else:
            im.putpixel((s, t), col)

    if filename:
        im.save('img/'+ filename +'.png')
    else:
        im.show()


def mandelbrot_set(C=-0.13 + 0.75j, pol=[1,0,0], filename='', julia=False, frame=[-2,-1.5,3], coloring=0):

    x0 = frame[0]
    y0 = frame[1]
    dt = frame[2]

    im     = Image.new("RGB", (1000, 1000), (255, 255, 255))
    colors = different_colors(31)
    weight = 0
    for s, t in product(xrange(1000), xrange(1000)):
        steps = 0
        if julia:
            z = x0 + s * dt / 1000. + (y0 + t * dt / 1000.) * 1j
        else:
            C = x0 + s * dt / 1000. + (y0 + t * dt / 1000.) * 1j
            z = 0

        for i in xrange(30):
            if abs(z) > 2:
                break
            z      = z**3 - z**2 + C
            steps += 1
        
        if coloring == 0:
            if abs(z) < 2:
                col = tuple(3 * [0])
                weight += 1
            else:
                col = tuple(3 * [255])
                weight -= 0.05

        elif coloring == 1:
            col = colors[(15 + steps) % 30]   
        #HSV_tuples = [(z.real * 1.0 /  31, 1, 0.85) for x in range(31) ]
        #RGB_tuples = map(lambda x: colorsys.hsv_to_rgb( *x ), HSV_tuples)
        #RGB_tuples = map(lambda x: tuple(map(lambda y: int(y * 255),x)),RGB_tuples)

        #if abs(z) < 2:
            #col = tuple(3 * [0])
        #col = tuple( map( lambda x: int(x), [255 * z.real, 255*z.imag, 255*(z.real + z.imag)]))
        #col = tuple( map( lambda x: int(x), [255*(steps), 255 * z.real, 255*z.imag]))
        #col = colors[steps]
        #else:
        #col = tuple(3 * [255])

        im.putpixel((s, t), col)

    #if weight < 0:
    #    print "Not enough points in the frame"
    #    print ">>> Weight: {}".format( weight )
    #    print ">>> C:      {}".format( C )
#
#    #    return
#    #else:
#    #    print "Enough points"
#    #    print ">>> Weight: {}".format( weight )
#    #    print "+++ {}".format( filename +'.png' )
    #    print ">>> C:      {}".format( C )

    if filename:
        im.save('img/'+ filename +'.png')
    else:
        im.show()


if __name__ == '__main__':

    newton_fractal(filename='newton_fractal')

    #frames = [[-2,-1.5,3],
    #          [-1,-1,1],
    #          [-.8,-.8,.5],
    #          [-.6,-.7,.1],
    #          [-.55,-.67,.01],
    #          [-.555,-.675,0.01]]

    #frames = [[-2,-0.5, 1],
    #          [-2,-0.5, .5],
    #          [-2,-0.5, .1],
    #          [-2,-0.5, .01]]

    #for frame in frames:
    #    filename  = 'mandelbrot_set'
    #    filename += '_'.join([str(x) for x in frame])
    #    mandelbrot_set(filename=filename, frame=frame, coloring=1)

#    k = 90
#    for x, y in product(range(1), range(90,101)):
#        #C = round(random(),2) + round(random(),2) * 1j
#        C = 0.38+ 0.01 * y * 1j 
#        #C = 0.38 + 0.98j
#        filename  = 'Ajulia_set_'+ str( k ).zfill( 4 )
#        #mandelbrot_set(C=C, filename=filename, julia=True,frame=[-2,-2,4], coloring=1)
#        k += 1
#
#        mandelbrot_set(C=C, filename=filename,julia=True, frame=[-2,-2,4], coloring=0)