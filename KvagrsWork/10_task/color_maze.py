#!/usr/bin/env python

from mazelib   import *
from num_maze  import *
from itertools import product
from numpy     import array

class ColorMaze(NumberMaze):

    def __init__ (self, maze):

        self.size  = maze[0][0]
        # from maze pop the size
        self.maze  = maze[1:]
        self.col_dict  = {}
        self.STACK = []
        self.paths = []

        # initialize the dictionary
        for i, j in product(xrange(self.size), xrange(self.size)):
            self.col_dict[ self.maze[i][j] ] = 0

        # fill the dictionary according to occurence of the colors
        for i, j in product(xrange(self.size), xrange(self.size)):
            self.col_dict[ self.maze[i][j] ] += 1

        # no need to check start, end and white squares
        del self.col_dict['A']
        del self.col_dict['Z']
        del self.col_dict['W']

        self.min_color = min( self.col_dict.values() )


    def DFS(self, pos):
    # deep-first search algorithm to solve color maze

        # if STACK is not empty check whether this path
        # did not used to much of some color
        if self.STACK:
            if not self.check_stack():
                return
        self.STACK.append( pos )

        if self.maze[pos[0]][pos[1]] == 'Z':
            # check the STACK
            if self.check_sum():
                # copy the STACK, since it reach the end
                self.paths.append( self.STACK[::] )
            # pop the last position
            self.STACK.pop()
            return
        else:
            for _dir in [[0,1],[1,0],[-1,0],[0,-1]]:
                new_pos = list( pos + array( _dir ) )
                #print "pos: {}, _dir {} new_pos: {} STACK:{}".format(pos, _dir, new_pos, self.STACK)
                # avoid cycles
                if new_pos in self.STACK:
                    continue
                if self.on_board( new_pos ) and new_pos not in self.STACK:
                    #print "on_board {}".format( new_pos )
                    self.DFS( new_pos )
            # if the path did not lead to the end
            else:
                self.STACK.pop()

    def tmp_STACK(self):

        # create a copy of the col_dict
        # initialized to zeros
        self.tmp_dict = self.col_dict.copy()
        for key in self.tmp_dict:
            self.tmp_dict[ key ] = 0

        # get the values from the STACK
        for pos in self.STACK:
            key = self.maze[pos[0]][pos[1]]
            if key in self.tmp_dict:
                self.tmp_dict[ key ] += 1

        # set the value to the first number of color
        self.tmp_value = self.tmp_dict[self.tmp_dict.keys()[0]]


    def check_stack(self):
    # check the path for to many steps on one color

        self.tmp_STACK()

        for key in self.tmp_dict:
            # False if some color is more then the minimal
            if self.tmp_dict[ key ] > self.min_color:
                return False
        else:
            return True


    def check_sum(self):
    # check the final sum of colors

        self.tmp_STACK()

        for key in self.tmp_dict:
            # False if some color is more then the minimal
            if self.tmp_dict[ key ] > self.min_color:
                return False
            # if some number of colors differs
            if self.tmp_value != self.tmp_dict[ key ]:
                return False
        # if for looped over everything
        else:
            return True


if __name__ == '__main__':

    mazes = load_col_maze('col_maze.txt')
    for maze in mazes:
        maze = ColorMaze( maze )
        maze.DFS([maze.size - 1, 0])
        for path in maze.paths:
            color_gif_path(maze.maze, maze.size, path, maze.col_dict, side=50)