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
        self.QUEUE    = []
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

    def all_walls(self):

        for point in self.walls:
            for _dir in self.dirs:
                new_point = list( point + _dir )
                if self.on_board( new_point ):
                    self.FIXED = list(point)
                    if self.DFS_cycle( new_point ):
                        self.toggle_wall( point, new_point, True)

        return


    def first_walls(self):

        tmp_walls = self.walls.copy()

        while tmp_walls:
            point = random.choice( tmp_walls.keys() )
            pos_dirs = [ _dir for _dir in self.dirs\
                        if self.on_board( point + _dir) == True and\
                        tuple(point + _dir ) in tmp_walls.keys()]
            if not pos_dirs:
                del tmp_walls[ point ]

            else:
                # choose one of possible directions
                _dir = random.choice( pos_dirs )

                new_point  = tuple(point + _dir)
                self.FIXED = list(point)
                #print self.DFS_cycle( new_point )
                self.toggle_wall(point, new_point, True)
                print self.DFS_cycle( new_point )
                if self.DFS_cycle( new_point ):
                    self.toggle_wall(point, new_point, False)

                del tmp_walls[ point ]
                del tmp_walls[ new_point ]

        return

    def check_cycles(self):

        for point in self.walls:
            for _dir in self.dirs:
                self.FIXED = list( point )
                new_point  = list( point + _dir )
                #print "point {} in dir {} is {}".format(point, _dir, new_point)
                if self.on_board( new_point ):
                    if list(point) == [9,9]:
                        print "point {} in dir {} is {}".format(point, _dir, new_point)
                        print self.DFS_cycle( new_point )
                    if self.DFS_cycle( new_point ) == False and self.is_wall(point, new_point):
                        self.toggle_wall(new_point, point, False)

                        #for _dir in self.dirs:and len( self.STACK) > 2
                        #    new_point  = list( point + _dir )
                        #    if self.on_board( new_point ):
                        #        self.toggle_wall( point, new_point, False)

        return


    def DFS_cycle(self, pos):

        self.STACK.append( pos )
        """
        # with fixed
        if list(pos) == list(self.FIXED) and len(self.STACK) > 2:
            self.STACK = []
            return True
        else:
            for _dir in self.dirs:
                new_point = list(pos + _dir)
                if self.on_board( new_point ) and\
                    self.is_wall(pos, new_point) == False:
                    self.STACK.append( new_point )
                    if list(new_point) == list(self.FIXED) and len(self.STACK) > 2:
                        self.STACK = []
                        return True
                    else:
                        self.DFS_cycle( new_point )
            else:
                self.STACK = []
        return False

        """

        """
        visited = [ list(pos) ]

        while visited != [ list(x) for x in self.walls.keys()]:
            pos = self.STACK.pop()
            for _dir in self.dirs:
                new_point = list(pos + _dir)
                if self.on_board( new_point ):
                    if self.walls[tuple(pos)][self.dir_to_wall[tuple(_dir)]] != True:
                        self.STACK.append( new_point )
                        visited.append( new_point )
                        if new_point == self.FIXED:
                            return True
        return False
        """


        """
        if not self.STACK:
            return False
        else:
            for _dir in self.dirs:
                new_point = list( pos + _dir)
                if self.walls[tuple(pos)][self.dir_to_wall[tuple(_dir)]] != True and\
                    self.on_board( new_point ):
                    self.STACK.append( new_point )
                    if new_point == self.STACK[0]:
                        self.STACK = []
                        return True
                    self.DFS_cycle( new_point )
            else:
                self.STACK = []
                return False

        """
        """
        visited = [pos]
        while self.STACK:
            pos = self.STACK.pop()
            if pos == self.FIXED and len( self.STACK ) > 2:
                self.STACK = []
                return True
            else:
                for _dir in self.dirs:
                    new_point = list(pos + _dir)
                    #print self.walls[pos][self.dir_to_wall[tuple(_dir)]] != False and\
                    #self.on_board( new_point )
                    if self.walls[tuple(pos)][self.dir_to_wall[tuple(_dir)]] != True and\
                        self.on_board( new_point ) and new_point not in visited:
                        visited.append( new_point )                    
                        self.STACK.append( new_point )
                    if len(self.STACK ) > 2 and self.FIXED == self.STACK[0]:
                        self.STACK = []
                        return True
                

        self.STACK = []
        return False
        """

        """
                        #if new_point in self.STACK:
                        #    return True

        
        if pos == self.FIXED and len( self.STACK) > 2:
            #self.STACK.pop()
            self.STACK = []
            return True
        else:
            for _dir in self.dirs:
                new_point = list(pos + _dir)
                #print self.walls[pos][self.dir_to_wall[tuple(_dir)]] != False and\
                #self.on_board( new_point )
                if self.walls[tuple(pos)][self.dir_to_wall[tuple(_dir)]] != True and\
                self.on_board( new_point ):
                    self.STACK.append( new_point )
                    print new_point in self.STACK and len( self.STACK) > 2
                    if len( self.STACK) > 2 and new_point == self.STACK[0]:
                        self.STACK = []
                        return True
                    else:
                        self.DFS_cycle( new_point )
            else:
                #self.STACK.pop()
                #self.STACK = []
                return False
        """
        
    def is_wall(self, point_A, point_B):
    # is wall between A and B?

        _dir = array( point_B ) - point_A
        wall = self.dir_to_wall[tuple(_dir)]
        if self.walls[tuple(point_A)][wall] == True:
            return True
        else:
            return False

    
    def toggle_wall(self, point_A, point_B, value=True):
    # adds wall between A and B

        _dir = array( point_B ) - point_A
        wall = self.dir_to_wall[tuple( _dir )]

        point_A = tuple(point_A)
        point_B = tuple(point_B)

        self.walls[point_A][wall] = value
        wall = (wall + 2) % 4
        self.walls[point_B][wall] = value

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
    #maze.walls = {(0,0): 4 * [False],
    #              (1,0): 4 * [False]}
    #maze.toggle_wall([0,0],[1,0])
    #print maze.walls

    maze.first_walls()
    maze.check_cycles()
    maze.FIXED = [9,9]
    print maze.DFS_cycle([8,9])
    print maze.DFS_cycle([9,8])
    #maze.all_walls()
    #maze.check_cycles()
    maze.bool_squares_to_lines()
    maze.draw_maze()