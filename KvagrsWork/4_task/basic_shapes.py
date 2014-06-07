#! usr/bin/env python

from PIL       import Image
from math      import tan, sqrt, pi, cos, sin, floor, ceil
from itertools import product


WHITE = (255,255,255)
BLACK = (0,0,0)

def circle(rad, x0=100, y0=100, fill=False, eps = 0.05):
# r = radius, the center of the circle = [x0,y0]

    coordinates = []
    for x in xrange(-rad,radd):
        for y in xrange(-rad,rad):
            if fill and x**2 + y**2 - r**2 <= eps :
                coordinates.append([x + x0,y + y0])
                print "fill"
            if ~fill and abs((x**2 + y**2 - r**2) / float(r**2)) <= eps:
                coordinates.append([x + x0,y + y0])

    return coordinates


def circle_par(r, start, end, thickness=20, fill=True):     # r = radius, start/end, absolute angles

    coordinates = []
    for t in xrange(start, end):
        r_t = (t * pi) / 180
        x = r + int(r * cos(r_t))
        y = r + int(r * sin(r_t))
        coordinates.extend(circle(thickness, x + r, y + r, fill))

    return coordinates


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
            col = tuple( map ( lambda x: int(127 * x), 3 * col))
            cols.append( col )

    pixs = pixs_and_cors(pixs, cols)

    return pixs


def spiral_par(start=0, end=3*360, thickness=3, fill=True):
# start/end, absolute angles

    # Calculate the offset
    #r_t = ((end%360)*pi)/180
    #a = int(end*cos(r_t) )
    #b = int(end*sin(r_t))
    coordinates = []
    for t in xrange(start, end):
        r_t = (t*pi)/180
        x = int(cos(r_t))
        y = int(sin(r_t))
        
        coordinates.extend(circle(thickness, x, y, fill))

    #print coordinates
    return coordinates


def equilateral_triangle(side):

    coordinates = []
    #print -side/2, side/2,int((sqrt(3)*side)/2)
    for x in xrange(-side / 2, side / 2):
        for y in xrange(int( (sqrt(3) * side) / 2)):
            alt = (sqrt(3) * side) / 2
            if y <= sqrt(3) * x + alt and y <= -sqrt(3) * x + alt:
                # minus y-coordinate - [0,0] is top left and pos. directions are v and >
                coordinates.append([x + side,-y + side])

    return coordinates


def pixs_and_cors(pixs, cols):
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

    im = Image.new("RGB", (size[0],size[1]), "white")
    for pix in pixs:
    #    r = pix[0]
    #    g = pix[1]
    #    b = pix[0] + pix[1]+100
    #    #b = (200)
#
#    #    color = (r,g,b)
        im.putpixel( pix[0], pix[1])

    if filename:
        im.save('img/'+ filename + '.png')
    else:
        im.show()


if __name__ == '__main__':

    #draw(circle(100, 300,300, fill=True), filename="circle_fill")
    #draw(circle(100, 300,300, fill=False), filename="circle")
    #draw(circle_par(100, 0, 360, thickness=5, fill=True), filename="circle_par")
    #draw(equilateral_triangle(100), filename="equilateral_triangleA")
    #draw(ellipse_par(100,50), filename="spiral_par")
    #draw(spiral_par()) 
        draw(ellipse(100, 50), 'ellipse')
    #ellipse(10, 5)