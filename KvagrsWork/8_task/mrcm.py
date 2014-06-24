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
    """

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

    """
    operators = [combine(scaling(0.255,0.255), translation(0,-270)),
                 combine(scaling(0.255,0.255), translation(-255,150)),
                 combine(scaling(0.255,0.255), translation( 255,150)),
                 combine(scaling(0.735,0.735), rotation(30)),
                 ]

    lines = MRCM(points, 5, operators)
    draw_and_save('star', lines)
    

    points = array([[-half, -half, 1],
                    [ half, -half, 1],
                    [ half, 2 * half, 1],
                    [-half, 2 * half, 1]])

    operators = [combine(scaling(0.85,0.85), rotation(3), translation(12,-30)),
                 combine(translation(100,150),rotation(45),scaling(0.4,0.5)),
                 combine(translation(-70,100),rotation(-50),scaling(0.35,0.4)),
                 combine(scaling(0.001,0.3),rotation(3), translation(12,720))]

#    operators = [combine(scaling(0.001,0.85), rotation(3), translation(12,-30)),
#                 combine(translation(100,150),rotation(45),scaling(0.001,0.5)),
#                 combine(translation(-70,100),rotation(-50),scaling(0.001,0.4)),
#                 combine(scaling(0.001,0.3),rotation(3), translation(12,720))]

    lines = MRCM(points, 6, operators)
    draw_and_save('barnsley_fern', lines)