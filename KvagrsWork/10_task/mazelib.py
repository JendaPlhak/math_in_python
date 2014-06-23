#!/usr/bin/env python

import sys
for i in xrange(1, 11):
    sys.path.append('../'+ str(i) +'_task')

from affine_transformation import connect_points
from numpy                 import array
from hide_and_seek         import download_file, PATH
from itertools             import product

import re
import svgwrite
import os


COLORS = {'W':'rgb(255,255,255)',
              'R':'rgb(255,10,10)',
              'Y':'rgb(255,255,10)',
              'B':'rgb(10,10,255)',
              'K':'rgb(0,0,0)',
              'O':'rgb(255,133,10)',
              'P':'rgb(133,10,255)',
              'N':'rgb(51,26,0)',
              'G':'rgb(0,153,0)',
              'A':'rgb(255,255,255)'}

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


def load_col_maze(filename, separator='-'):
# loads the color maze

    with open(filename, 'r') as f:
        mazes = f.read().rstrip()

    if separator:
        mazes = re.split(r'%s+'%separator, mazes)

    #print mazes
    mazes_table = []
    while mazes:
        maze = []
        tmp_maze = mazes.pop().rstrip()[::-1].rstrip()[::-1]
        for row in tmp_maze.split('\n'):
            maze.append( row.split() )

        print maze
        maze[0][0] = int(maze[0][0])
        mazes_table.append( maze )

    """
    print mazes_table


    #size = tmp_maze[0]
    #tmp_maze = tmp_maze[2:]

    maze = []
    for row in tmp_maze.split('\n'):
        maze.append( row.split() )

    maze[0][0] = int(maze[0][0])

    return maze
    """
    return mazes_table


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

    for x, y in product(xrange(size), xrange(size)):
        im.add( im.text(maze[x][y],
                        insert      = text_offset([y, x], side),\
                        font_family ="sans-serif",\
                        font_size   = side / 2,\
                        fill        ='black'))

    return


def addColors(im, maze, size, side=20):
# fills the squares with color
# available colors 
# white, red, yellow, blue, black(K), orange, purple
# brown(N), green
    
    colors = {'W':'rgb(255,255,255)',
              'R':'rgb(255,10,10)',
              'Y':'rgb(255,255,10)',
              'B':'rgb(10,10,255)',
              'K':'rgb(0,0,0)',
              'O':'rgb(255,133,10)',
              'P':'rgb(133,10,255)',
              'N':'rgb(51,26,0)',
              'G':'rgb(0,153,0)',
              'A':'rgb(255,255,255)'}

    for i, j in product(xrange(size), xrange(size)):
        corner = tuple(side * array( [j, i] ))
        if maze[i][j] == 'Z':
            draw_chessboard(im, corner, side)
        else:
            im.add( im.rect(insert = corner,\
                            size   = (side, side),\
                            fill   = colors[maze[i][j]]))


    return


def draw_chessboard(im, corner, side):

    fifth   = side / 5.
    corners = [[fifth, 0], [0, fifth],
               [2 * fifth, fifth],
               [fifth, 2 * fifth],
               [3 * fifth, 0],
               [0, 3 * fifth],
               [4 * fifth, fifth],
               [fifth, 4 * fifth],
               [3 * fifth, 2 * fifth],
               [2 * fifth, 3 * fifth],
               [3 * fifth, 4 * fifth],
               [4 * fifth, 3 * fifth]
               ]

    corners = [ list(array(x) + corner) for x in corners ]

    for corner in corners:
        im.add( im.rect(insert = corner,\
                        size   = (fifth, fifth),\
                        fill   = 'black'))

    return


def text_offset(point, side):
# offsets so the numbers will be nicely in the middle

    point = [ point[0] * side + side * 0.35, point[1] * side + side * 0.65 ]
    return point


def put_path_to_string(path):
# from path of type list creates str
# [[0,0],[3,0]] --> '0-0_3-0'
# useful to distinguish same maze with different solution

    str_path = ''
    for point in path:
        str_path += '_'
        str_path += str(point[0]) +'-'+ str(point[1])

    return str_path


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


def number_gif_path(maze, size, path, side=20, type_path=''):
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


def draw_color_maze(maze, side=20, save=True):
# draws svg color maze
    
    im   = svgwrite.drawing.Drawing()
    size = maze[0][0]
    maze = maze[1:]

    addColors(im, maze, size, side)
    addGrid(im, size, side)

    if save:
        im.saveas('img/color_maze.svg')
    return


def color_gif_path(maze, size, path, step_dict, side=20, type_path=''):
# draws the path given by the DFS from ColorMaze class
        
    print "Creating gif from: "
    for row in maze:
        print "  "+ " ".join( [str(x) for x in row])

    im = svgwrite.drawing.Drawing()
    # reverse x, y because of the canvas nature
    path = [x[::-1] for x in path]

    # create lines from path and scale them
    lines = connect_points( path )[:-1]
    lines = [list( side * array(x) + 4 * [side / 2]) for x in lines]
    linewidth = side / 10
    lines = expand_lines( lines, linewidth / 2)

    # draw the rest
    addColors(im, maze, size, side)
    addGrid(im, size, side)

    # reverse x, y because of the step counter
    path = [x[::-1] for x in path]

    # add the step counter
    #steps = [[(size + 1) * side, (side * 1.3) * y] for y in xrange(len(step_dict))]
    counter_corners = dict.fromkeys( step_dict.keys(),0 )
    for i, key in enumerate(counter_corners ):
        counter_corners[ key ] = [(size + 1) * side, (side * 1.3) * i]

    print counter_corners
    for i, key in enumerate( step_dict ):
        im.add( im.rect(insert = counter_corners[ key ],\
                        size   = (side, side),\
                        stroke = 'black',\
                        fill   = COLORS[ key ]))

    count_dict = dict.fromkeys( step_dict.keys(), 0 )
    #for key in count_dict:
    #    count_dict[key] = 0

    #print count_dict

    for i, last in enumerate( lines ):
        # draw the lines you have passed
        for passed in lines[:i + 1]:
            im.add( im.line(start  = passed[:2],\
                            end    = passed[2:],\
                            style  = 'stroke:black; stroke-width:'+ str(linewidth) +';' ))

        # increment if step is on color
        maze_value = maze[path[i + 1][0]][path[i + 1][1]]
        if maze_value in count_dict.keys():
            count_dict[ maze_value ] += 1
            im.add( im.rect(insert = counter_corners[ maze_value ],\
                        size   = (side, side),\
                        stroke = 'black',\
                        fill   = COLORS[ maze_value ]))
            im.add( im.text(count_dict[maze_value],\
                            insert = counter_corners[maze_value] + array([side * 0.35, side * 0.65]),\
                            font_family = 'sans-serif',\
                            font_size = side / 2,\
                            fill = 'black'))

        index = str(i + 1).zfill( len( str( len( lines))))
        filename = 'img/color_gif_'+ index +'.svg'
        print "+++ {}".format( filename )
        im.saveas( filename )

    
    # convert svg files to gif
    print ">>> converting to gif:"
    gifname = str(size) +'_'+ str(size) + put_path_to_string( path )
    build   = 'convert -delay 72 img/color_gif_*.svg img/'+ gifname +'.gif'
    os.system( build )

    # do the clean up
    for f in sorted( [fn for fn in os.listdir('img/') if fn.startswith('color_gif_')]):  
        print "--- {}".format( 'img/'+ f )
        os.remove( 'img/'+ f )
    
    return



def expand_lines(lines, shift):

    for i, line in enumerate( lines ):
        if line[0] == line[2]:
            if lines[i][1] < lines[i][3]:
                lines[i][1] -= shift
                lines[i][3] += shift
            else:
                lines[i][1] += shift
                lines[i][3] -= shift
        else:
            if lines[i][0] < lines[i][2]:
                lines[i][0] -= shift
                lines[i][2] += shift
            else:
                lines[i][0] += shift
                lines[i][2] -= shift

    return lines


if __name__ == '__main__':

    """
    download_file( PATH +'ciselne-bludiste.txt')
    maze = load_num_maze('ciselne-bludiste.txt', separator='-')
    for i, m in enumerate(maze):
        print "Drawing maze number {}.".format(i + 1)
        draw_number_maze(maze=m, num=(i + 1), side=50)
    """

    maze = load_col_maze('col_maze.txt')
    draw_color_maze(maze, side=50)