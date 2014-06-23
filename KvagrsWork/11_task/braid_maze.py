#!/usr/bin/env python
import sys
import os

for i in xrange(1,11):
    sys.path.append('../'+ str(i) +'_task')

from num_maze import NumberMaze
from numpy    import array

import random
import svgwrite

class BraidMaze(NumberMaze):
# inheritance for self.on_board()

    def __init__(self, filename, size, side=20):

        self.filename = filename
        self.size     = size
        self.side     = side
        self.points  = [[4 * [True] for x in xrange(size)] for y in xrange(size)]
        self.lines    = []

    def first_lines(self):

        tmp_points = self.points[::]

        point = random.choice([ random.choice( self.points )])
        print point

        #while tmp_points:
        #    point = random.choice([ random.choice( self.points )])
        #    print point
        #    tmp_points.remove( point )


        return 

    def bool_squares_to_lines(self):

        for i, row in enumerate( self.points ):
            for j, square in enumerate( row ):
                if square[0]:
                    A = list(self.side * array([i, j]))
                    B = list(self.side * array([i, j]) + [self.side, 0])
                    line = A + B
                    if all( l for l in [line, line[2:] + line[:2]]) not in self.lines:
                        self.lines.append( line )
                if square[1]:
                    A = list(self.side * array([i, j]) + [self.side, 0])
                    B = list(self.side * array([i, j]) + [self.side, self.side])
                    line = A + B
                    if all( l for l in [line, line[2:] + line[:2]]) not in self.lines:
                        self.lines.append( line )
                if square[2]:
                    A = list(self.side * array([i, j]) + [0, self.side])
                    B = list(self.side * array([i, j]) + [self.side, self.side])
                    line = A + B
                    if all( l for l in [line, line[2:] + line[:2]]) not in self.lines:
                        self.lines.append( line )
                if square[3]:
                    A = list(self.side * array([i, j]))
                    B = list(self.side * array([i, j]) + [0, self.side])
                    line = A + B
                    if all( l for l in [line, line[2:] + line[:2]]) not in self.lines:
                        self.lines.append( line )

        return

    def draw_maze(self):

        im = svgwrite.drawing.Drawing()

        linewidth = str(self.side / 12.)
        for line in self.lines:
            im.add( im.line(start = line[:2],\
                            end   = line[2:],\
                            style = 'stroke:black; stroke-width:'+ linewidth +';'))

        im.saveas('img/braid_maze.svg')

        return

if __name__ == '__main__':

    maze = BraidMaze('braid_maze', 4)
    maze.bool_squares_to_lines()
    maze.first_lines()