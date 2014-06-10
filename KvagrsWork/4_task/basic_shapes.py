#!/usr/bin/env python

import sys
for i in xrange(1,11):
    sys.path.append('../'+ str(i) +'_task/')

from PIL                  import Image
from math                 import tan, sqrt, pi, cos, sin, floor, ceil
from itertools            import product
from segment_intersection import dist


WHITE = (255,255,255)
BLACK = (0,0,0)

def pyth(x, y):
    return (x**2 + y**2)**0.5


def circle(r, x0=100, y0=100, fill=False, eps= 0.05):
# r = radius, the center of the circle at [x0, y0]

    pixs = []
    cols = []
    for x in xrange(-r, r):
        for y in xrange(-r, r):

            if fill and x**2 + y**2 - r**2 <= eps :
                pixs.append([x + x0,y + y0])
                if abs((x**2 + y**2 - r**2) / float(r**2)) <= eps:                
                    col = tuple( map( lambda x: int(x), 3 * [255 * sin(pyth(x, y) / pi)]))
                else:
                    col = BLACK
                cols.append( col )

            if  not fill and abs((x**2 + y**2 - r**2) / float(r**2)) <= eps:
                pixs.append([x + x0,y + y0])
                col = tuple( map( lambda x: int(x), 3 * [127 * (-cos(pyth(x, y)) + 1)]))
                cols.append( col )

    pixs = pixs_and_cols(pixs, cols)

    return pixs


def circle_par(r, start, end, thickness=20, fill=True):
# r = radius, start/end, absolute angles

    pixs = []
    cols = []
    for t in xrange(start, end):
        r_t = (t * pi) / 180
        x = int(r_t * cos(r_t))
        y = int(r_t * sin(r_t))
        pixs.append([ x + r, y + r])
        #cols.append( BLACK )
        col = tuple( map( lambda x: int(x), [y, x + y, x]))
        cols.append( col )

    pixs = pixs_and_cols(pixs, cols)

    return pixs


def ellipse_par(a, b, start=0, end=360, thickness=5, fill=True):
# a, b axis, start/end, absolute angles

    coordinates = []
    for t in xrange(start, end):
        # Convert degrees to radians
        r_t = (t*pi)/180
        # Calculate coordinates
        x = a + int(a * cos(r_t))
        y = b + int(b * sin(r_t))
        coordinates.extend(circle(thickness, x + a, y + b, fill))

    return coordinates


def ellipse(a, b, eps=0.05):

    pixs = []
    cols = []
    for x, y in product(range(-a*2, a*2), range(- 2*b, 2*b)):
        n_a = a * 1.
        n_b = b * 1.

        if (x / n_a)**2 + (y / n_b)**2 + (x * y) / (n_a * n_b) - 1 <= eps:
            pixs.append( [x, y] )
            col = [sin( (x / (n_a) )**2 + (y / n_b)**2 + (x * y) / (n_a * n_b))]
            col = tuple( map ( lambda x: int(255 * x), 3 * col))
            cols.append( col )

    pixs = pixs_and_cols(pixs, cols)

    return pixs


def spiral_par(start=0, end=1080, fill=True):
# start/end, absolute angles

    # Calculate the offset
    #r_t = ((end%360)*pi)/180
    #a = int(end*cos(r_t) )
    #b = int(end*sin(r_t))
    pixs = []
    cols = []
    for t in xrange(start, end):
        r_t = (t * pi) / 180
        x = 50 * int(cos(r_t))
        y = 50 * int(sin(r_t))
        
        pixs.append([x, y])
        cols.append( BLACK )
        #pixs.extend(circle(thickness, x, y, fill))
    pixs = pixs_and_cols(pixs, cols)
    #print pixs
    return pixs


def equilateral_triangle(side):

    pixs = []
    cols = []
    t1   = [-side / 2, 0]
    t2   = [ side / 2, 0]
    t3   = [ 0, (sqrt(3) * side) / 2]

    for x in xrange(t1[0], t2[0]):
        for y in xrange(int( t3[1] )):
            alt = t3[1]
            if y <= sqrt(3) * x + alt and y <= -sqrt(3) * x + alt:
                # minus y-coordinate - [0,0] is top left and pos. directions are v and >
                pixs.append([x + side,-y + side])
                col = tuple( map( lambda x: int(2.3 * x), [ dist([x, y], t1),\
                                                            dist([x, y], t2),\
                                                            dist([x, y], t3),]))

                cols.append( col )
    pixs = pixs_and_cols(pixs, cols)

    return pixs


def pixs_and_cols(pixs, cols):
# shifts pixels and then adds corresponding colors

    pixs, size = movePointsTowardsOrigin( pixs )
    pixs       = [ size ] + [ [pixs[i], cols[i]] for i in xrange(len(pixs))]

    return pixs


def movePointsTowardsOrigin(points):

    minX = points[0][0]
    minY = points[0][1]
    maxX = points[0][0]
    maxY = points[0][1]

    for point in points:
        if minX > point[0]: minX = point[0]
        if minY > point[1]: minY = point[1]
        if maxX < point[0]: maxX = point[0]
        if maxY < point[1]: maxY = point[1]

    minA = min(minX, minY)

    for point in points:
        point[0] -= minX
        point[1] -= minY

    # determine the size of the canvas
    size = [ maxX - minX + 1, maxY - minY + 1]

    return points, size 


def draw(pixs, filename=''):
    
    size = pixs[0]
    pixs = pixs[1::]
    im   = Image.new("RGB", (size[0],size[1]), "white")
    for pix in pixs:
        im.putpixel( pix[0], pix[1])

    if filename:
        im.save('img/'+ filename + '.png')
    else:
        im.show()


if __name__ == '__main__':

    #draw(circle(100, 300,300, fill=True), filename="circle_fill")
    #draw(circle(100, 300,300, fill=False), filename="circle")
    draw(circle_par(100, 0, 5000), filename="circle_par")
    #draw(equilateral_triangle(100), filename="triangle_fun")
    #draw(ellipse_par(100,50), filename="spiral_par")
    #draw(spiral_par(), filename='spiral') 
    #draw(ellipse(100, 50), 'ellipse')
    #ellipse(10, 5)