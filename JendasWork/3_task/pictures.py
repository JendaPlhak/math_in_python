#!/usr/bin/env python
from turtle import Turtle
from math   import atan, sqrt, pi
from cmath  import exp


def square(draw, rec, a=100, shift=0.7):

    j = 0
    while j < rec:
        for i in xrange(4):
            draw.forward(a)
            draw.right(90)

        draw.forward(a * shift)

        draw.right(pi/2 - atan( (1-shift)/shift ), rad=True)
        
        a  = a * sqrt((1-shift)**2 + shift**2)
        j += 1


def barredCircle(draw, r=500, shift=10):

    x0 = draw.coord.real
    y0 = draw.coord.imag

    n_points = int(2*r / shift) * 2 # Number of points symmetrically distributed on the circle

    step   = 2 * pi / n_points
    points = []
    for i in xrange(n_points):
        z = r * exp(1j*i*step)
        draw.addLine(z + draw.coord, z.conjugate() + draw.coord)
        z = r * exp(1j*(i*step + 0.5 * step))
        draw.addLine(z + draw.coord, z - 2*z.real + draw.coord)
        

def triangle(draw, rec, a=10, space=10):

    j = 0
    center = draw.coord
    while j < rec:
        j += 1
        draw.penUp()
        draw.left(90)
        draw.forward((2/3.) * (a**2 * 3/4 )**0.5)
        draw.right(180 - 30)
        draw.penDown()

        for i in xrange(3):
            draw.forward(a)
            draw.right(180 - 60)

        a += space
        draw.resetDir()
        draw.setCoord(center.real, center.imag)


def rose(draw, a=30, n = 12):

    angle = (n-2) * 180. / n
    k = 18
    for _ in xrange(k):
        for i in xrange(n):
            draw.forward(a)
            draw.right(180 - angle)
        draw.right(360./k)



if __name__ == "__main__":

    draw = Turtle("Various_pictures")

    draw.setCoord(250, 250)
    draw.resetDir()

    draw.penDown()
    square(draw, 200)

    draw.resetDir()
    draw.setCoord(500, 250)
    barredCircle(draw, r=50, shift=5)

    draw.setCoord(750, 250)
    triangle(draw, 10, 5, 15)

    draw.setCoord(1000, 250)
    rose(draw)

    draw.penUp()
    draw.dumpImage()





