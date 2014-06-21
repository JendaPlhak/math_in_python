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


def draw_number_maze(maze, num, side=20):

    size = maze[0][0]
    maze = maze[1::]
    im   = svgwrite.drawing.Drawing()

    # grid
    for i in xrange( size - 1):
        A = [ side * (i + 1), 0]
        B = [ side * (i + 1), size * side]

        im.add( im.line(start  = A,\
                        end    = B,\
                        stroke = 'gray'))
        im.add( im.line(start  = A[::-1],\
                        end    = B[::-1],\
                        stroke = 'gray'))
    # outline
    corners = array( [[0,0], [1, 0], [1,1], [0,1]] )
    for i in xrange(4):
        corners[i] *= size * side

    for line in connect_points( corners ):
        im.add( im.line(start  = line[:2],\
                        end    = line[2:],\
                        stroke = 'black'))

    # fill maze with numbers
    for x, y in itertools.product(xrange(size), xrange(size)):
        im.add( im.text(maze[x][y],
                        insert      = text_offset([y, x], side),\
                        font_family ="sans-serif",\
                        font_size   = side / 2,\
                        fill        ='black'))


    im.saveas('img/'+ str(num) +'_maze_'+ str(size) +'.svg')

    return


def text_offset(point, side):

    point = [ point[0] * side + side * 0.35, point[1] * side + side * 0.65 ]
    return point


if __name__ == '__main__':

    download_file( PATH +'ciselne-bludiste.txt')
    maze = load_num_maze('ciselne-bludiste.txt', separator='-')
    for i, m in enumerate(maze):
        print "Drawing maze number {}.".format(i + 1)
        draw_number_maze(maze=m, num=(i + 1), side=50)