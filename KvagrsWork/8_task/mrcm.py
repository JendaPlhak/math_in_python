#!/usr/bin/env python

from affine_transformation import *
from numpy                 import array
from itertools             import product
from math                  import atan2
from PIL                   import Image, ImageDraw

def MRCM(group, rep, operators):

    A_queue = [ group ]
    lines   = connect_points( group )
    #lines = []

    for i in xrange(rep):
        B_queue = []
        while A_queue:
            group = A_queue.pop()
            for operator in operators:
                tmp_group = []
                for point in group:
                    tmp_group.append( dot(operator, point) )
                B_queue.append( tmp_group )
        if (i + 1) == rep:
            lines.extend( [y for x in B_queue for y in  connect_points( x )])

        A_queue = B_queue[::]


    return lines
        

if __name__ == '__main__':

    side = 250
    half = side / 2
    # Sierpinski relatives
    #points = array([[0,0,1],[side,0,1],[side,side,1],[0,side,1]])
    points = array([[-half, -half, 1],
                    [ half, -half, 1],
                    [ half,  half, 1],
                    [-half,  half, 1]])

    list_operators = [[translation(-half, -half),
                       translation(-half,  half),
                       translation( half,  half)],

                      [combine(translation(-half,-half), reflexion(1,-1)),
                       combine(translation(-half, half)),
                       combine(translation(half, half), reflexion(-1,1))],

                      [combine(translation(-half,-half), reflexion(-1,1)),
                       combine(translation(-half, half)),
                       combine(translation(half, half), reflexion(1,-1))],

                      [combine(translation(-half,-half), reflexion(-1,-1)),
                       combine(translation(-half, half)),
                       combine(translation(half, half), reflexion(-1,-1))],
                     ]

    #for i, operators in enumerate( list_operators ):
    #    for j in xrange( len(operators) ):
    #        operators[j] = combine(scaling(0.5,0.5), operators[j])
#
#    #    lines = MRCM(points, 8, operators)
    #    plot_and_save('sierpinski_rel_'+ str(i + 1), lines)

    #points = array([[0,0,1],[side,0,1],[side,side,1],[0,side,1]])
    operators = [combine(scaling(0.255,0.255), translation(37.26, 67.14)),
                 combine(scaling(0.255,0.255), translation(11.46, 22.32)),
                 combine(scaling(0.255,0.255), translation(63.06, 22.32))]
    lines = MRCM(points, 2, operators)
    plot_and_save('star', lines)