#!/usr/bin/env python

import sys
for i in xrange(1,11):
    sys.path.append('../'+ str(i) +'_task/')

from lib_turtle            import *
from math                  import tan, cos, sin, acos, pi
from affine_transformation import connect_points


def pythagoras(side, angle, a):

    angle   = radians( angle )
    side_A  = side + a * cos( angle ) * 1.
    side_B  = a * sin( angle )
    squares = side_A**2 + side_B**2

    return squares**0.5, side_A, side_B


def pentagram_rel(turtle, side):

    for i in xrange(5):
        turtle.forward(side)
        turtle.left(72)


    turtle.right( 180 - ((5 + 1) / 2 * 360. / 5 ))
    for x in xrange(5):
        turtle.forward( pythagoras(side, 72, side)[0] )
        turtle.right( ((5 + 1) / 2 * 360. / 5 ))

    return


def pentagram_abs(turtle, side):

    polygon(turtle, side)
    points = turtle.coords
    turtle.restart()

    vex  = points.pop()
    while points:   
        for point in points:
            turtle.line( vex + point )
        vex = points.pop()
    
    return
    

def inf_polygon(turtle, side, shift, n=4, rep=2):

    out_angle = 360. / n
    A, B      = pythagoras(side - shift, out_angle, shift)[1:]
    angle     = degrees( atan2(B, A) )

    for i in xrange(rep):
        polygon(turtle, side, n)
        turtle.penup()
        turtle.forward( shift )
        turtle.pendown()
        turtle.left( angle )

        tmp   = side
        side  = pythagoras(side - shift, out_angle, shift)[0]
        shift = side / tmp * shift * 1.

    return


def grid_circle(turtle, rad, n):

    step = rad / (n - 1) * 2.
    x    = -rad

    for i in xrange(n):
        y  = ( round(rad**2 - x**2) )**0.5
        vertical   = [x, y, x, -y]
        horizontal = [y, x, -y, x]

        turtle.line( horizontal )
        turtle.line( vertical )
        x += step

    return 


def Triangles(turtle, side=20, step=20, n=5):

    for i in xrange(n):
        x  = side / 2 - i * step / tan(pi / 6)
        y1 = step * i
        y2 = -(side**2 - side**2/4)**0.5 - i * step / sin(pi / 6)


        points = [[ -x, y1],
                  [  x, y1],
                  [  0, y2 ]]

        for line in connect_points( points ):
            turtle.line( line )
        

    return


def triangles(turtle, side=100, step=20, n=5):
    for i in xrange(n):
        #print side
        side += (3*step)
        #print side
        polygon(turtle, side, 3)
        turtle.right(120)
        turtle.penup()
        turtle.forward(step)
        turtle.left(120)
        turtle.back(step)
        turtle.pendown()
    return


def polycircle(turtle, n=12):
    for x in xrange(n):
        polygon(turtle, 30, n)
        turtle.left(360. / n)
    return


if __name__ == '__main__':

    
    turtle = Turtle()
    
    pentagram_rel(turtle, 200)
    turtle.draw_object('pentagram_rel')

    turtle.restart()
    pentagram_abs(turtle, 100)
    turtle.draw_object('pentagram_abs')
    
    
    for i in [4, 7, 14]:
        turtle.restart()
        inf_polygon(turtle, 100., 75., i,rep=25)
        turtle.draw_object('inf_polygon_'+ str(i))
    
    for i in [15, 29]:
        turtle.restart()
        grid_circle(turtle, 100., i)
        turtle.draw_object('grid_circle_'+ str(i))

    turtle.restart()
    triangles(turtle, 20, 5, 20)
    turtle.draw_object('triangles')

    for i in [12, 42]:
        turtle.restart()
        polycircle(turtle, i)
        turtle.draw_object('polycircle_'+ str(i) )