#!/usr/bin/env python

from mazelib       import *
from itertools     import product
from hide_and_seek import download_file, PATH

class NumberMaze():

    def __init__(self, maze):
        self.start       = [0,0]
        self.size        = maze[0][0]
        self.maze        = maze[1:]
        self.paths       = []
        self.STACK       = []
        self.lowest_sum  = 0
        self.highest_sum = 0
        self.low_paths   = []
        self.high_paths  = []

    def DFS(self, pos):
    # deep-first search algorithm
    # keeping the stack outside the function
    # to be able to copy it to get the path

        self.STACK.append( pos )

        # check for the end position, that is right
        # bottom corner
        if self.maze[pos[0]][pos[1]] == 0:
            # get the path
            self.paths.append( self.STACK[::] )
            self.STACK.pop()
            return
        else:
            for _dir in [[0,1],[1,0],[-1,0],[0,-1]]:
                # jump to the next position
                new_pos = list( pos + self.maze[pos[0]][pos[1]] * array( _dir ))
                # avoid cycles
                if new_pos in self.STACK:
                    continue
                if self.on_board( new_pos ) and new_pos not in self.STACK:
                    self.DFS( new_pos )
            # if the path did not lead to the end
            else:
                self.STACK.pop()

        return


    def calc_sums(self):
    # goes through all possible solutions/paths
    # and filters those with lowest and highest
    # path_sum()

        if self.paths:
            self.lowest_sum  = self.path_sum( self.paths[0] )
            self.highest_sum = self.path_sum( self.paths[0] )
        else:
            print "No paths found."

        for path in self.paths:
            self.lowest_sum  = min(self.lowest_sum,  self.path_sum( path ))
            self.highest_sum = max(self.highest_sum, self.path_sum( path ))

        self.low_high_paths()

        return self.lowest_sum, self.highest_sum


    def path_sum(self, path):
    # returns the sum of jumps of the given path

        path_sum = 0
        for point in path:
            path_sum += self.maze[point[0]][point[1]]

        return path_sum


    def low_high_paths(self):
    # goes through paths and finds the one with
    # lowest and highest path_sum()

        for path in self.paths:
            if self.path_sum( path ) == self.lowest_sum:
                self.low_paths.append( path )

            if self.path_sum( path ) == self.highest_sum:
                self.high_paths.append( path )

        return



    def on_board(self, pos):
    # False if the position pos is of outside the grid

        if any(x < 0 for x in pos) or any(x  > self.size - 1 for x in pos):
            return False
        else:
            return True 


if __name__ == '__main__':

    # download the file, necessary for server
    download_file( PATH + 'ciselne-bludiste.txt')

    mazes = load_num_maze('ciselne-bludiste.txt', '-')


    for maze in mazes:
        maze  = NumberMaze( maze )
        # magic is here
        maze.DFS([0,0])
        maze.calc_sums()

        # creates animated gif for different paths with
        # lowest and highest sum of "jumps"
        for path in maze.low_paths:
            gif_path(maze.maze, maze.size, path, 30, 'low')
    
        for path in maze.high_paths:
            gif_path(maze.maze, maze.size, path, 30, 'high')