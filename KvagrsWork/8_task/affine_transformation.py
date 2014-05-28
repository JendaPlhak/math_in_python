#! usr/bin/env python

import sys
sys.path.append('../4_task/')

from basic_shapes   import movePointsTowardsOrigin
from math           import sin, cos
from numpy          import array, matrix, pi, dot, empty, concatenate
from PIL            import Image

import svgwrite


def translation(t_x, t_y):

    trans_matrix = array([ [1, 0, t_x ],
                           [0, 1, t_y ],
                           [0, 0,  1  ] ])
    return trans_matrix


def rotation(alfa):

    # convert to radians for sin,cos
    alfa       = (alfa * pi) / 180.
    rot_matrix = array([ [cos(alfa), -sin(alfa), 0 ],
                         [sin(alfa),  cos(alfa), 0 ],
                         [0,          0,         1 ] ])
    return rot_matrix


def reflexion(r_x=1, r_y=1):

    ref_matrix = array([ [ r_x,  0,  0 ],
                         [  0,  r_y, 0 ],
                         [  0,   0,  1 ] ])
    return ref_matrix


def scaling(s_x=1, s_y=1):

    scal_matrix = array([ [ s_x, 0,  0 ],
                          [  0, s_y, 0 ],
                          [  0,  0,  1 ] ])
    return scal_matrix


def shear(k_x=0, k_y=0):

    shear_matrix = array([ [  1,  k_x, 0 ],
                           [ k_y,  1,  0 ],
                           [  0,   0,  1 ]])
    return shear_matrix


def combine(*args):
    # calculates the matrix of all affine transformations from *args

    # matrices are multiplied from 
    matrix = args[ len(args) - 1 ]
    for i in xrange( len(args) ):
        matrix = dot( args[ len(args) - (i + 1) ], matrix)

    return matrix


def iterate_transformation(points, iteration=1, matrix=array([[1,0,0],[0,1,0],[0,0,1]])):

    lines = connect_points( points )

    for i in range(iteration):
        new_points = []
        for point in points:
            point = dot(matrix, point)
            new_points.append( point )
        points = new_points      
        lines.extend( connect_points( points ) ) # new_points
    return lines


def connect_points(points):

    lines = []
    for i in range( len(points) ):
        lines.append( concatenate( ( points[ i ][:2], points[ (i + 1) % len(points) ][:2]) , axis=0 ) )
    return lines


def min_max_lines(lines):
    # returns min x and y coordinate from lines

    lines = zip(*lines)

    x_coords = [x for a in lines[0:][::2] for x in a]
    y_coords = [y for b in lines[1:][::2] for y in b]

    x_min = min(x_coords)
    x_max = max(x_coords)
    y_min = min(y_coords)
    y_max = max(y_coords)

    return x_min, y_min


def min_max_points(points):

    points = [x for y in points for x in y]

    x_min = min(points)
    x_max = max(points)
    y_min = min(points)
    y_max = max(points)

    return  x_min, y_min


def shift_lines(lines):

    min_x, min_y = min_max_lines(lines)

    for line in lines:
        line[0] -= min_x
        line[2] -= min_x
        line[1] -= min_y
        line[3] -= min_y

    return lines


def plot_and_save(filename, lines=[], points=[]):

    if lines:
        im    = svgwrite.drawing.Drawing()
        lines = shift_lines( lines )

        for line in lines:
            im.add( im.line(start = line[:2],\
                            end   = line[2:],\
                            stroke= 'black'))
        im.saveas('img/'+ filename +'.svg')

    if points:
        pass
        
        #im = Image.new("RGB", )

    return


if __name__ == '__main__':

    
    points   = array([[0,0,1],[100,0,1],[100,100,1],[0,100,1]])

    # First example from http://www.fi.muni.cz/~xpelanek/IV122/slidy/lingebra.pdf
    operator = combine(rotation(20), scaling(1.1, 1.1), translation(5, 10))
    lines = iterate_transformation(points, iteration=10, matrix=operator)   
    plot_and_save('1_example', lines)

    # Second example from http://www.fi.muni.cz/~xpelanek/IV122/slidy/lingebra.pdf
    operator = combine(rotation(10), scaling(1.1, 0.8))
    lines = iterate_transformation(points, iteration=15, matrix=operator)   
    plot_and_save('2_example', lines)

    # Third example from http://www.fi.muni.cz/~xpelanek/IV122/slidy/lingebra.pdf
    operator = combine(shear(1.3), rotation(10), scaling(0.9,0.9),translation(50, 50))
    lines = iterate_transformation(points, iteration=25, matrix=operator)   
    plot_and_save('3_example', lines)



    #operator = translation(10, 10)
    #operator =  reflexion(-1)
    operator = scaling(0.5,0.5)
    #operator = rotation(30)
    #operator = shear(1, 0)
    #operator = shear(0, 1)
    #operator = combine(translation(25,25), scaling(0.5, 0.5))
    lines = iterate_transformation(points, iteration=1, matrix=operator)
    plot_and_save('example', lines)