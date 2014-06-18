#!/usr/bin/env python
import sys
for i in xrange(1, 12):
    sys.path.append('../'+ str(i) +'_task')


import svgwrite
from random                 import random, randint
from math                   import sqrt, cos, sin, atan, acos, pi
from segment_intersection   import cross_point, generate_data, dist
from polygon                import determinant
#from basic_shapes           import movePointsTowardsOrigin
from affine_transformation  import shift_points, shift_lines, min_max_points
import math


def find_right(points):
# find the rightest point in the plane

    right = points[0]

    for point in points:
        if right[0] <= point[0]:
            right = point
    return right


def norm(u):

    return ( dot_product(u, u) )**0.5


def dot_product(u,v):

    S = 0
    for i in xrange( len(u) ):
        S += u[i] * v[i]

    #if S == 0:
        #print u, v
    return S


def angle(u,v):

    arg = ( dot_product(u,v) / (norm(u) * norm(v)) )

    return acos(arg)



def degToRad(phi):      # Conversion function from degrees to radians
        r_phi = (phi * pi) / 180
        return r_phi


def vectorize(A,B):

    u0 = B[0]-A[0]
    u1 = B[1]-A[1]

    return [u0, u1]


def line_print(data):

    for item in data:
        print data


def smallest_angle(vector, fixed, points):

    dangle = angle( fixed, points[0])
    k     = 0
    for i, point in enumerate(points):
        if 180 - angle( vector, vectorize(fixed, points[i]) ) < dangle:
            dangle = angle( vector, points[i] )
            k = i

    return points[ k ]


def convex_wrapping(n=50, data=[]):

    if not data:
        data = generate_data( n )

    fixed = find_right( data )
    data.remove( fixed )
    next  = smallest_angle( [0,1], fixed, data)
    lines = [ fixed + next ]
    print "FIXED1 {}".format( fixed )
    print "NEXT1 {}".format( next )

    while fixed != next:
        data.append( fixed )
        vector = vectorize( fixed, next )
        #print data
        fixed = next
        data.remove( fixed )
        #print "FIXED {}".format( fixed )
        next  = smallest_angle( vector, fixed, data)
        #print "NEXT {}".format( next )
        lines.append( fixed + next )


    """

    points        = generate_data(n)            # generate points in plane
    backup_points = points                      # backup for return
    
    r_point = find_right(points)                # find the rightest point
    #fixed_v    = vectorize([0,1], r_point)         # starting vector to which will be calculated the angle

    points.remove(r_point)                      # remove the r_point from points, but put it back later so it can cycle
    next = points[0]                            # get the first point, why not. No need for random

    edges   = []
    fixed_v = vectorize([0,1], r_point)
    free_v  = vectorize(next, r_point)
    _angle   = angle(fixed_v, free_v)

    while next != r_point:
        for point in points:
            free_v  = vectorize(point, r_point)
            n_angle = angle(fixed_v, free_v)
            if _angle > n_angle:
                next  = point
                _angle = n_angle

        edges.append(r_point + next)
        points.append(r_point)
        r_point = next
        points.remove( r_point )

    """


    return data, lines


def draw_data(points=[], lines=[]):

    #points = shift_points( points )
    line_print(lines)
    lines  = shift_lines( lines, min_max_points( points )[:2] )
    points = shift_points( points )
    line_print(lines)

    im     = svgwrite.drawing.Drawing()
    for point in points:
        im.add( im.circle(center = point,\
                          r      = 5,\
                          fill   = 'blue'))
    #im.add( im.circle(center = find_right( points ),\
    #                  r      = 5,\
    #                  fill   = 'red'))
#
#    #im.add( im.circle(center = points[ smallest_angle( find_right(points), points) ],\
#    #                  r      = 5,\
    #                  fill   = 'purple'))

    for line in lines:
        #print line
        im.add( im.line(start  = line[:2],\
                        end    = line[2:],\
                        stroke = 'green'))

    im.saveas('img/data.svg')
    return


if __name__ == '__main__':


    data = [[200,100],[0,300],[-200,-100],[100,0]]

    #data.remove([100,0])
    #print smallest_angle([100,0], data) 
    #points, lines = convex_wrapping(20)
    #draw_data( data )
    points, lines = convex_wrapping()
    draw_data( points, lines )
    #for i in xrange(21):
    #   t = math.pi / 2 + math.pi / 20 * i 
    #   print "For angle {}".format( math.degrees( t) )
    #   print ">>> {}".format( angle([1,0],[cos(t), sin(t)]) )
    #   print ">>> {}".format( math.degrees( angle([1,0], [cos(t), sin(t)]) ) )

    print math.degrees(angle([-1,1],[-1,-2]))
    #print vectorize([2,1],[0,3])