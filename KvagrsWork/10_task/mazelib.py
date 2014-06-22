#!/usr/bin/env python

import sys
for i in xrange(1, 11):
    sys.path.append('../'+ str(i) +'_task')

from affine_transformation import connect_points
from numpy                 import array
from hide_and_seek         import download_file, PATH

import itertools
import re
import svgwrite
import os


def load_num_maze(filename, separator=''):

    with open( filename, 'r') as f:
        maze = f.read().rstrip()

    if separator:
        maze = re.split(r'%s+'%separator, maze)

    for i, m in enumerate(maze):
        maze[i] = m.rstrip()[::-1].rstrip()[::-1]

    maze_table = []
    while maze:
        tmp_maze  = maze.pop()
        tmp_table = []

        for line in tmp_maze.split('\n'):
            row = [int(a) for a in line.split() if a.isdigit()]
            tmp_table.append(row)

        maze_table.append( tmp_table )

    return maze_table


def addGrid(im, size, side=20):
# draws the grid
    
    # grid
    for i in xrange( size - 1):
        A = [ side * (i + 1), 0]
        B = [ side * (i + 1), size * side]

        im.add( im.line(start  = A,\
                        end    = B,\
                        stroke = 'rgb(50,50,50)'))
        im.add( im.line(start  = A[::-1],\
                        end    = B[::-1],\
                        stroke = 'rgb(50,50,50)'))

    # outline
    corners = array( [[0,0], [1, 0], [1,1], [0,1]] )
    for i in xrange(4):
        corners[i] *= size * side

    for line in connect_points( corners ):
        im.add( im.line(start  = line[:2],\
                        end    = line[2:],\
                        stroke = 'black'))

    return


def addNumbers(im, maze, size, side=20):
# fill maze with numbers

    for x, y in itertools.product(xrange(size), xrange(size)):
        im.add( im.text(maze[x][y],
                        insert      = text_offset([y, x], side),\
                        font_family ="sans-serif",\
                        font_size   = side / 2,\
                        fill        ='black'))

    return


def text_offset(point, side):
# offsets so the numbers will be nicely in the middle

    point = [ point[0] * side + side * 0.35, point[1] * side + side * 0.65 ]
    return point


def draw_number_maze(maze, num, side=20, save=True):
# draws the given number maze, expected as list of lists of ints
    
    # get the values and declare canvas
    size = maze[0][0]
    maze = maze[1::]
    im   = svgwrite.drawing.Drawing()

    # self-explanatory
    addGrid(im, size, side)
    addNumbers(im, maze, size, side)

    if save:
        im.saveas('img/'+ str(num) +'_maze_'+ str(size) +'.svg')        

    return


def gif_path(maze, size, path, side=20, type_path=''):
# draws the path square by square and gifs it

    print "Creating gif from: "
    for row in maze:
        print "  "+ " ".join( [str(x) for x in row])

    for i, stand in enumerate( path ):
        im   = svgwrite.drawing.Drawing()
        for passed in path[:i]:
            corner = array( passed ) * side
            im.add( im.rect(insert = corner[::-1],\
                            size   = (side, side),\
                            fill   = 'rgb(102,178,255)' ))

        corner = array( stand ) * side
        im.add( im.rect(insert = corner[::-1],\
                        size   = (side, side),\
                        fill   = 'rgb(0,102,204)' ))
        addGrid(im, size, side)
        addNumbers(im, maze, size, side)

        num   = str(i + 1).zfill( len( str( len( path ))))
        _file = 'img/maze_gif_'+ num +'.svg'
        print "+++ {}".format( _file )
        im.saveas( _file )

    # convert svg files to gif
    print ">>> converting to gif:"
    gifname = str(size) +'_'+ type_path + put_path_to_string( path )
    build   = 'convert -delay 72 img/maze_gif_*.svg img/'+ gifname +'.gif'
    os.system( build )

    # do the clean up
    for f in sorted( [fn for fn in os.listdir('img/') if fn.startswith('maze_gif_')]):  
        print "--- {}".format( 'img/'+ f )
        os.remove( 'img/'+ f )
    return


def put_path_to_string(path):
# from path of type list creates str
# [[0,0],[3,0]] --> '0-0_3-0'
# useful to distinguish same maze with different solution

    str_path = ''
    for point in path:
        str_path += '_'
        str_path += str(point[0]) +'-'+ str(point[1])

    return str_path


if __name__ == '__main__':

    download_file( PATH +'ciselne-bludiste.txt')
    maze = load_num_maze('ciselne-bludiste.txt', separator='-')
    for i, m in enumerate(maze):
        print "Drawing maze number {}.".format(i + 1)
        draw_number_maze(maze=m, num=(i + 1), side=50)