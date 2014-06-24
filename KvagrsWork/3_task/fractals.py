#!/usr/bin/env python

from lib_turtle import Turtle, polygon, radians
from math       import sin, pi

import time
import numpy as np

def rev_polygon(turtle, n, side):

    for i in xrange(n):
        turtle.forward( side )
        turtle.right( 360. / n)

    return

def tree(turtle, n, step):

    if n == 1:
        turtle.forward( step )
    else:
        turtle.forward( step )
        pos  = [ turtle.x, turtle.y ]
        _dir = turtle.phi

        for rot in [45, -45]:
            turtle.set_pos( pos )
            turtle.set_dir( _dir )
            turtle.right( rot )
            tree( turtle, n - 1, step / 2.)

    return

    
def koch(turtle, n, step):

    if n == 1:
        turtle.forward( step )
    else:
        step = step / 3 
        for rot in [0, 60, -120, 60]:
            turtle.left( rot )
            koch(turtle, n - 1, step)

    return


def koch_snowflake(turtle, n, step):

    for i in xrange(3):
        koch(turtle, n, step)
        turtle.right(120)

    return


def sierpinski(turtle, order, side):


    A1 = [ 0, 0]
    A2 = [ side / 2., 0]
    A3 = [ side / 4.,  - 3**0.5 / 4. * side]

    if order == 1: 
        polygon(turtle, side, 3)
    else:   
        side /= 2
        shift = np.array( [turtle.x, turtle.y])
        for pos in [ A1, A2, A3]:
            pos += shift
            turtle.set_pos( pos )
            sierpinski(turtle, order - 1, side)
        
    return

def anchors(side, pos=[0, 0], _dir=0):
# 0.381 is a magic constant

    myrtle = Turtle()
    myrtle.set_pos( pos )
    myrtle.set_dir( _dir )
    rev_polygon(myrtle, 5, side )
    myrtle.coords.pop(0)
    myrtle.forward( side * 0.381 )
    myrtle.coords.pop()
    myrtle.right( 72 )
    myrtle.forward( side * 0.381 )
    myrtle.dots = myrtle.coords[::]

    return myrtle.coords


def pentaflake(turtle, order, side):

    if order == 1:
        rev_polygon(turtle, 5, side)
    else:
        part = side * 0.381
        pos  = [ turtle.x, turtle.y ]
        _dir = turtle.phi
        rot  = 5 * [ 72 ] + [36]
        for i, anchor in enumerate(anchors(side, pos, _dir)):
            turtle.set_pos( anchor )
            turtle.right( rot[i] )
            pentaflake(turtle, order - 1, part)
        turtle.set_dir( _dir )
        turtle.set_pos( pos )
        
    return


# possible something a bit interesting
def side_effect_1(turtle, order, side):

    if order == 1:
        polygon(turtle, side, 5)
    else:
        pos  = [ turtle.x, turtle.y ]
        _dir = turtle.phi
        for i in xrange(10):
            #turtle.set_pos( pos )
            turtle.forward( side )
            turtle.right( 72 )
            pentaflake(turtle, order - 1, side)
        turtle.penup()
        turtle.forward( side )
        turtle.left( 72 )
        turtle.forward( side )
        turtle.right( 36 )
        turtle.forward( side )
        turtle.left( 72 )
        turtle.forward( side )
        turtle.right(72)
        turtle.pendown()

    return


def side_effect_2(turtle, order, side):

    if order == 1:
        polygon(turtle, side, 5)
    else:
        pos  = [ turtle.x, turtle.y ]
        _dir = turtle.phi
        for i in xrange(5):

            pentaflake(turtle, order - 1, side * 1.6)
            turtle.right( 72 )
            turtle.forward( side )
    return


def side_effect_3(turtle, order, side):

    if order == 1:
        rev_polygon(turtle, 5, side)
    else:
        half = side / 2
        pos  = [ turtle.x, turtle.y ]
        _dir = turtle.phi
        for i in xrange(5):
            pentaflake(turtle, order - 1, half)
            turtle.penup()
            step = 2 * half * (1 + sin(radians(18))) 
            turtle.forward( step )
            turtle.pendown()
            turtle.right( 72 )

        turtle.set_pos( pos )
        turtle.penup()
        step = 2 * side * (1 + sin(radians(18))) 
        turtle.forward( step )
        turtle.pendown()
        turtle.right( 72 )


if __name__ == '__main__':
        
    
    print "Sending turtle Bilbo on an adventure!"
    Bilbo = Turtle()

    """
    print ">>> Bilbo sees a tree fractal.."
    Bilbo.left( 90 )
    clock = time.time()
    tree(Bilbo, 6, 250)
    print "    Time: {}".format(time.time() - clock)
    Bilbo.draw_object('tree')
    Bilbo.restart()

    print ">>> Bilbo found Koch snowflake.."
    clock = time.time()
    koch_snowflake(Bilbo, 4, 450)
    print "    Time: {}".format(time.time() - clock)
    Bilbo.draw_object('koch')
    Bilbo.restart()
    
    print ">>> Bilbo tripped over Sierpinski basket.."
    clock = time.time()
    sierpinski(Bilbo, 5, 500)
    print "    Time: {}".format(time.time() - clock)
    Bilbo.draw_object('sierpinski')
    Bilbo.restart()

    print ">>> Bilbo sees is amazed by pentagonal snowflake.."
    clock = time.time()
    pentaflake(Bilbo, 4, 300)
    print "    Time: {}".format(time.time() - clock)
    Bilbo.draw_object('pentaflake_4')
    """

    side_effect_1(Bilbo, 4, 100)
    Bilbo.draw_object('side_effect_1')

    Bilbo.restart()
    side_effect_2(Bilbo, 4, 100)
    Bilbo.draw_object('side_effect_2')

    Bilbo.restart()
    side_effect_3(Bilbo, 4, 100)
    Bilbo.draw_object('side_effect_3')