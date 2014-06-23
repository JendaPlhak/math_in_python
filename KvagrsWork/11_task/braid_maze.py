#!/usr/bin/env python
import sys
import os

for i in xrange(1,11):
    sys.path.append('../'+ str(i) +'_task')

from num_maze               import NumberMaze
from numpy                  import array
from affine_transformation  import connect_points

import random
import svgwrite

class BraidMaze(NumberMaze):
# inheritance for self.on_board()

    def __init__(self, filename, size, side=20):

        self.filename = filename
        self.size     = size
        self.side     = side
        #self.walls  = [[4 * [True] for x in xrange(size)] for y in xrange(size)]
        self.walls    = {}
        self.STACK    = []
        self.FIXED    = None
        # initialize maze without walls
        for i in xrange(size):
            for j in xrange(size):
                self.walls[(i,j)] = 4 * [False]

        self.lines    = []

        # translations between different views
        # one is as walls 0-3, the other is directions
        self.wall_to_dir = {0: array([ 0,-1]),
                            1: array([ 1, 0]),
                            2: array([ 0, 1]),
                            3: array([-1, 0])}

        self.dir_to_wall = {( 0,-1): 0,
                            ( 1, 0): 1,
                            ( 0, 1): 2,
                            (-1, 0): 3}

        self.dirs = [array(_dir) for _dir in [[0,-1],[1,0],[0,1],[-1,0]]]

        return




    def first_lines(self):

        tmp_walls = self.walls.copy()

        while tmp_walls:
            point = random.choice( tmp_walls.keys() )
            pos_dirs = [ _dir for _dir in self.dirs\
                        if self.on_board( point + _dir) == True and\
                        tuple(point + _dir ) in tmp_walls.keys()]
            if not pos_dirs:
                #tmp_walls.remove( walls )
                del tmp_walls[ point ]

            else:
                # choose one of possible directions
                _dir = random.choice( pos_dirs )
                new_point  = tuple(point + _dir)
                self.FIXED = point
                #print self.DFS_cycle( new_point )
                if self.DFS_cycle( new_point ):
                    self.toggle_wall(point, new_point)

                del tmp_walls[ point ]
                del tmp_walls[ new_point ]

        return

    def check_cycles(self):

        for point in self.walls:
            for _dir in self.dirs:
                self.FIXED = list( point )
                new_point  = list( point + _dir)
                if self.on_board( new_point ):
                    if self.DFS_cycle( new_point ) == False:
                        self.walls[tuple(point)] = 4 * [False]

        return


    def DFS_cycle(self, pos):

        self.STACK.append( pos )

        if pos == self.FIXED:
            self.STACK.remove( pos )
            return True
        else:
            for _dir in self.dirs:
                new_point = list(pos + _dir)
                #print self.walls[pos][self.dir_to_wall[tuple(_dir)]] != False and\
                #self.on_board( new_point )
                if self.walls[tuple(pos)][self.dir_to_wall[tuple(_dir)]] != True and\
                self.on_board( new_point ):
                    if new_point in self.STACK:
                        return True
                    else:
                        self.DFS_cycle( new_point )
            else:
                self.STACK.remove( pos )
                return False
        return False


        """
            wall  = random.randint(0,3)
            self.walls[ point ][wall] = True
            #print list(point)
            #print self.wall_to_dir[ wall ]
            new_point = list( point[::] + self.wall_to_dir[ wall ])
            if self.on_board( new_point ):
                new_point = tuple( new_point )
                wall = (wall + 2) % 4
                self.walls[ new_point ][wall] = True
                #del tmp_points[ new_point ]
                if new_point in tmp_points.keys():
                    tmp_points[ new_point ]

            del tmp_points[ point ]
            


        print self.walls


        return 
        """

    #def toggle_wall(self, point, wall):
    def toggle_wall(self, point_A, point_B, value=True):
    # adds wall between A and B

        _dir = array( point_B ) - point_A
        wall = self.dir_to_wall[tuple( _dir )]

        self.walls[point_A][wall] = value
        wall = (wall + 2) % 4
        self.walls[point_B][wall] = value

        """
        self.walls[point][wall] = True
        _dir = self.wall_to_dir[ wall ]
        adjacent = tuple(point + _dir)
        wall = (wall + 2) % 4
        self.walls[adjacent][wall] = True
        """

        return

    def bool_squares_to_lines(self):

        for key in self.walls:
        #for i, row in enumerate( self.walls ):
            #for j, square in enumerate( row ):
            if self.walls[ key ][0]:
                A = list(self.side * array( key ))
                B = list(self.side * array( key ) + [self.side, 0])
                line = A + B
                if all( l for l in [line, line[2:] + line[:2]]) not in self.lines:
                    self.lines.append( line )
            if self.walls[ key ][1]:
                A = list(self.side * array( key ) + [self.side, 0])
                B = list(self.side * array( key ) + [self.side, self.side])
                line = A + B
                if all( l for l in [line, line[2:] + line[:2]]) not in self.lines:
                    self.lines.append( line )
            if self.walls[ key ][2]:
                A = list(self.side * array( key ) + [0, self.side])
                B = list(self.side * array( key ) + [self.side, self.side])
                line = A + B
                if all( l for l in [line, line[2:] + line[:2]]) not in self.lines:
                    self.lines.append( line )
            if self.walls[ key ][3]:
                A = list(self.side * array( key ))
                B = list(self.side * array( key ) + [0, self.side])
                line = A + B
                if all( l for l in [line, line[2:] + line[:2]]) not in self.lines:
                    self.lines.append( line )

        return

    def draw_maze(self):

        im = svgwrite.drawing.Drawing()

        # draw walls/lines
        linewidth = str(self.side / 12.)
        for line in self.lines:
            im.add( im.line(start = line[:2],\
                            end   = line[2:],\
                            style = 'stroke:black; stroke-width:'+ linewidth +';'))

        # draw outline
        points = [[0,0],[1,0],[1,1],[0,1]]
        for i in xrange( len(points) ):
            points[i] = array( points[i] ) * (self.size * self.side)
        lines = connect_points( points )
        for line in lines:
            im.add( im.line(start = line[:2],\
                            end   = line[2:],\
                            style = 'stroke:black; stroke-width:'+ linewidth +';'))            


        im.saveas('img/'+ self.filename +'.svg')

        return

if __name__ == '__main__':

    maze = BraidMaze('braid_maze', 10)
    maze.first_lines()
    maze.check_cycles()
    maze.bool_squares_to_lines()
    maze.draw_maze()