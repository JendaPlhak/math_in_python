#!usr/bin/env python

import sys
for i in xrange(1,12):
    sys.path.append('../'+ str(i) +'_task/')

from basic_shapes   import movePointsTowardsOrigin
from pascals_triangle import different_colors

from math           import sin, cos
from numpy          import array, matrix, pi, dot, empty, concatenate
from PIL            import Image

import svgwrite


IDENTITY = array([[1,0,0],[0,1,0],[0,0,1]])

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

    shear_matrix = array([ [  1,  k_y, 0 ],
                           [ k_x,  1,  0 ],
                           [  0,   0,  1 ] ])
    return shear_matrix


def combine(*transf):
    # calculates the matrix of all affine transformations from *transf

    transf = list( transf )
    #print "Printing transformations.."
    #for item in transf:
    #    print "Item:"
    #    print item
    #print "Done."
    
    matrix = transf.pop()
    while transf:
        matrix = dot(transf.pop(), matrix)

    #print "Combined matrix: "
    #print "{}".format(matrix)
    
    return matrix


def line_transformation(points, group=True, iteration=1, matrix=IDENTITY):

    if group:
        lines = connect_points( points )
    else:
        all_points = list( points )

    for i in xrange(iteration):
        new_points = []
        for point in points:
            point = dot(matrix, point)
            new_points.append( point )
        points = list(new_points)

        if group:
            lines.extend( connect_points( points ) )
        else:
            all_points.extend(points)


    if group:
        return lines
    else:
        return all_points
    

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
    #x_max = max(x_coords)
    y_min = min(y_coords)
    #y_max = max(y_coords)

    return [x_min, y_min]


def min_max_points(points, shift=array([0,0])):

    points = [x for y in points for x in y]

    x_min = min(points)
    x_max = max(points) - x_min
    y_min = min(points)
    y_max = max(points) - y_min

    return  array([x_min, y_min, x_max, y_max])


def shift_lines(lines, shift=array([0,0])):

    x_min, y_min = min_max_lines( lines )

    #print "using shift {}".format( shift )
    if shift.any():
        print "using shift {}".format( shift )
        x_min, y_min = shift

    #print "Shifting lines.."
    #print "X min {}, Y min {}".format(x_min, y_min)
    for line in lines:
        #print "Line:{} ==> ".format(line)
        line[0] -= x_min
        line[2] -= x_min
        line[1] -= y_min
        line[3] -= y_min
        #print "==>  {}".format(line)
    return lines


def shift_points(points):

    x_min, y_min = min_max_points( points )[:2]

    for point in points:
        point[0] -= x_min
        point[1] -= y_min

    return points


def plot_and_save(filename, lines=[], points=[]):

    if lines:
        im     = svgwrite.drawing.Drawing()
        lines  = shift_lines( lines )
        colors = different_colors( len(lines) )

        for i, line in enumerate( lines ):
            im.add( im.line(start = line[:2],\
                            end   = line[2:],\
                            stroke= 'rgb'+ str(colors[ i ]) ))
        im.saveas('img/'+ filename +'.svg')

    if points:
        # watch out shift points changed
        size   = shift_points( points )[:2]
        print "size {}".format(size)
        im     = Image.new("RGB", size)
        points = shift_points( points )
        colors = different_colors( len( points ) )

        for i, point in enumerate( points ):
            im.putpixel(point, colors[ i ])
            im.save('img/'+ filename +'.png')

    return


if __name__ == '__main__':

    
    points = array([[0,0,1],[50,0,1],[50,50,1],[0,50,1]])
        
    # First example from http://www.fi.muni.cz/~xpelanek/IV122/slidy/lingebra.pdf
    operator = combine(rotation(20), scaling(1.1, 1.1), translation(5, 10))
    operator = combine(translation(5, 10), scaling(1.1, 1.1), rotation(20))
    lines = line_transformation(points, iteration=10, matrix=operator)   
    plot_and_save('1_example', lines)
    

    points = array([[-50, -50,1],[50,-50,1],[50,50,1],[-50,50,1]])
    # Second example from http://www.fi.muni.cz/~xpelanek/IV122/slidy/lingebra.pdf
    operator = combine(rotation(10), scaling(1.1,0.8))
    #operator = combine(scaling(1.1, 0.8), rotation(10))
    lines = line_transformation(points, iteration=15, matrix=operator)   
    plot_and_save('2_example', lines)
    
    # Third example from http://www.fi.muni.cz/~xpelanek/IV122/slidy/lingebra.pdf
    #operator = combine(shear(1.3), rotation(10), scaling(0.9,0.9),translation(50, 50))
    operator = combine(translation(50, 50), scaling(0.9, 0.9), rotation(10), shear(1.3))
    lines = line_transformation(points, iteration=25, matrix=operator)   
    plot_and_save('3_example', lines)
    

    #operator = translation(10, 10)
    #operator =  reflexion(-1)
    operator = scaling(0.95,0.95)
    operator = combine( operator )
    #operator = rotation(30)
    #operator = shear(1, 0)
    #operator = shear(0, 1)
    #operator = combine(translation(25,25), scaling(0.5, 0.5))
    points = line_transformation(points, group=False, iteration=50, matrix=operator)
    plot_and_save('example', points=points)