#!/usr/bin/env python
import sys
for i in xrange(8):
    sys.path.append('../' + str(i) + '_task')

from turtle_lib      import Turtle
from math            import sqrt, ceil, cos, sin, atan, degrees

import itertools
import svgwrite


def sieve_of_eratosthenes(n):           # returns list of first n primes

    numbers = [True] * n
    i       = 2
    while i**2 < n:
        for j in range(2, int(n / i) + 1):
            numbers[ ( i * j ) - 1 ] = False
        i += 1

    primes = []
    for j in range(1, n):
        if numbers[j] == True:
            primes.append(j + 1)

    return primes


def calculate_viewBox(coords, side):    # viewBox for the final svg

    _min = coords[0][0]
    _max = coords[0][0]

    for coord in coords:
        _min = min(_min, coord[0], coord[1])
        _max = max(_max, coord[0], coord[1])

    _max   += abs(_min) + side
    viewBox = ' '.join( str(x) for x in 2*[_min] + 2*[_max] )

    return viewBox, 2*[_max]


def get_steps(n, x_scale=0, useTriangle=False, useHex=False):   

    # returns list of steps for different shapes of spiral
    if useTriangle:
        tmp = range(1, n)       # sum( tmp ) > n
    elif useHex:
        tmp = 5*[1] + [2,1] + 4*[2] + [3]
        tmp.extend( [ x + i for i in range(1,n) for x in tmp[len(tmp)-6:] ] )
    else:    
        l_x, l_y  = [ i + x_scale for i in range(1, n/2) ], range(1, n/2)
        tmp = [ item for pair in zip(l_x, l_y) for item in pair ]   # sum( tmp ) > n

    for i, item in enumerate( tmp ):
        n -= item
        if n - tmp[ i + 1] < 0:
            tmp = tmp[ :i + 1 ]
            break

    tmp.append(n)
    return tmp


def coords_for_square(ulam, side):      # offset of the squares highlightning primes etc.

    for coord in ulam.coords:
        coord[0] -= side / 2.
        coord[1] -= side / 2.
    return


def hex_spiral(ulam, n, side):

    ord_a = side                           # calculate ordinates
    ord_b = side / 2.
    angle = degrees( atan(ord_b / ord_a) ) # calculate the angle

    ulam.right(90 + angle)
    for i, item in enumerate( get_steps(n, side, useHex=True) ):
        for j in range(item):
            if (i + 1) % 6 in [2, 5]:
                ulam.forward( side )
            else:
                ulam.forward( (ord_a**2 + ord_b**2 )**0.5 )

        if (i + 1) % 6 in [1, 2, 4, 5] and i != 0:
            ulam.left( 90 - angle )
        elif (i + 1) % 6 in [0, 3]:
            ulam.left( 2 * angle)
        else:
            ulam.left( 90 + angle )
        
    coords_for_square( ulam, side )
    return


def triangle_spiral(ulam, n, side):

    ord_a = side                           # calculate ordinates
    ord_b = side / 2.
    angle = degrees( atan(ord_b / ord_a) ) # calculate the angle

    ulam.right(90 + angle)
    for i in get_steps(n, side, useTriangle=True):
        for j in range(i):
            if i % 3 == 2:
                ulam.forward( side )
            else:
                ulam.forward( (ord_a**2 + ord_b**2 )**0.5 )
        if i % 3 == 0:
            ulam.left(180 - 2 * angle)
        else:
            ulam.left(90 + angle)

    coords_for_square( ulam, side )
    return


def rect_spiral(ulam, n, side, x_scale):

    for i in get_steps(n, x_scale):
        for j in range(i):
            ulam.forward( side ) 
        ulam.left(90)
    coords_for_square( ulam, side )
    return


def text_offset(point, side):        # off set for numbers
    return [ point[0], point[1] + side ]


def draw_ulam_spiral(n, side    =20,    x_scale =0,\
                     useTriangle=False, useHex  =False,\
                     addText    =False, addLines=False, addSquares=True,\
                     modulo     =0,     filename=''):

    ulam = Turtle()

    if modulo:
        numbers = range(0, n + 1, modulo)
    else:
        numbers = sieve_of_eratosthenes(n + 1)
        

    if useTriangle:
        triangle_spiral(ulam, n, side)
    elif useHex:
        hex_spiral(ulam, n, side)
    else:
        rect_spiral( ulam, n, side, x_scale)

    viewBox, size =  calculate_viewBox(ulam.coords, side)
    im            = svgwrite.drawing.Drawing( size=size, viewBox=viewBox )

    for i, point in enumerate(ulam.coords):
        if addSquares:
            if i + 1 in numbers:
                im.add(im.rect(insert = point,\
                               size   = (side, side),\
                               fill   = '#335588'))
        if addText:
            im.add( im.text(i+1,
                            insert      = text_offset( point, side ),\
                            font_family ="sans-serif",\
                            font_size   =10,\
                            fill        ='black'))
    if addLines:
        for line in ulam.lines:
            im.add(im.line(start  = line[:2],\
                           end    = line[2:],\
                           stroke = 'black'))

    im.saveas('img/'+ filename +'.svg')
    return


if __name__ == '__main__':

    """
    # Basic ulam_spiral: example, primes, modulo
    draw_ulam_spiral(20,\
                     side    =20,   addText   =True,\
                     addLines=True, addSquares=False,\
                     filename='square_spiral_example')

    draw_ulam_spiral(100000,\
                     side    =2, addSquares=True,\
                     filename='square_spiral_primes')

    draw_ulam_spiral(1000,\
                     side  =2, addSquares=True,\
                     modulo=4, filename  ='square_spiral_modulo')

    # Basic ulam_rect_spiral: example, primes, modulo
    draw_ulam_spiral(20,\
                     side      =20,    x_scale =5,\
                     addText   =True,  addLines=True,\
                     addSquares=False, filename='rect_spiral_example')
    """
    draw_ulam_spiral(100000,\
                     side      =2,    x_scale =111,\
                     addSquares=True, filename='rect_spiral_primes')

    draw_ulam_spiral(10000,\
                     side      =2,    x_scale=111,\
                     addSquares=True, modulo =7,\
                     filename  ='rect_spiral_modulo')
    """
    # Basic ulam_triangle_spiral: example, primes, modulo
    draw_ulam_spiral(20,\
                     side      =20,    addText    =True,\
                     addLines  =True,  useTriangle=True,\
                     addSquares=False, filename   ='triangle_spiral_example')

    draw_ulam_spiral(100000,\
                     side      =2,    useTriangle=True,\
                     addSquares=True, filename   ='triangle_spiral_primes')

    draw_ulam_spiral(10000,\
                     side      =2,    useTriangle=True,\
                     addSquares=True, modulo     =2,\
                     filename  ='triangle_spiral_modulo')

    # Basic ulam_hex_spiral: example, primes, modulo
    draw_ulam_spiral(20,\
                     side      =20,    addText =True,\
                     addLines  =True,  useHex  =True,\
                     addSquares=False, filename='hex_spiral_example')

    draw_ulam_spiral(100000,\
                     side      =2,    useHex  =True,\
                     addSquares=True, filename='hex_spiral_primes')

    draw_ulam_spiral(10000,\
                     side      =2,    useHex=True,\
                     addSquares=True, modulo=8,\
                     filename  ='hex_spiral_modulo')
"""