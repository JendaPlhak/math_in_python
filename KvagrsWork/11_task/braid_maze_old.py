#!/usr/bin/env python
import sys
import os

for i in xrange(1,11):
    sys.path.append('../'+ str(i) +'_task')

from num_maze import NumberMaze
from numpy    import array

import random
import svgwrite

class BraidMazeOld(NumberMaze):
# inherits on_board

    def __init__(self, filename='braid_maze', size=10, side=50):
        self.size     = size
        self.points   = [[x, y] for x in xrange(size) for y in xrange(size)]
        self.lines    = []
        self.side     = side
        self.filename = filename
        self.dirs     = [ array(_dir) for _dir in  [[0,1],[0,-1],[1,0],[-1,0]]]

        self.STACK    = []

        # add the first line to each point
        tmp_points = self.points[::]
        #print tmp_points
        while tmp_points:
            # choose point
            point = random.choice( tmp_points )
            # get all possible directions
            true_dir = [ _dir for _dir in self.dirs\
                        if self.on_board( point + _dir ) ==  True and\
                        list(point + _dir) in tmp_points]
            # remove if you can not add any more lines from point
            if not true_dir:
                tmp_points.remove( point )
            else:
                # choose one of possible
                _dir = random.choice( true_dir )
                self.lines.append( point + list(point + _dir) )
                # to avoid squares (more like minimaze)
                tmp_points.remove( point )
                tmp_points.remove( list(point + _dir) )

        return


    def add_lines(self):

        # create all possible lines
        all_lines = []
        for point in self.points:
            for _dir in self.dirs:
                new_point = list( point + _dir )
                if self.on_board( new_point ):
                    all_lines.append( point + new_point )

        # randomly choose a line, if without stop, add it
        while all_lines:
        #for line in all_lines:
            line = random.choice( all_lines )
            if self.check_for_U_stop( line ):
                print self.check_for_U_stop( line )
                self.lines.append( line )
            all_lines.remove( line )

        return

    def check_for_U_stop(self, line):
    # checks, if by adding line to self.lines
    # a U-shape end appears or not

        tmp_lines = self.lines[::]
        tmp_lines.append( line )
    # watch out for lines of board!
        for c_line in tmp_lines:
            A = c_line[:2]
            B = c_line[2:]
            if self.is_horizontal( c_line ):
                print "is_horizontal"
                #print "is_horizontal", line
                # check for vertical directions
                for _dir in self.dirs[:2]:
                    line_A = A + list(A + _dir)
                    line_B = B + list(B + _dir)
                    #print all([line_A, line_B]) in self.lines
                    #if all([line_A, line_B]) in self.lines:
                    if all( l in tmp_lines for l in [line_A, line_B]):
                        return False
            else:
                print "is_vertical"
                for _dir in self.dirs[2:]:
                    line_A = A + list(A + _dir)
                    line_B = B + list(B + _dir)
                    if all( l in tmp_lines for l in [line_A, line_B]):
                    #if all([line_A, line_B]) in self.lines:
                        return False

        return True


    def is_horizontal(self, line):
    # determines, whether line is __ or |

        if line[1] == line[3]:
            #print line
            return True
        else:
            return False        


    def is_cycle(self, point):
    # determine, whether there is a cycle after
    # a wall is added
        self.STACK.append( point )

        for _dir in self.dirs:
            new_point = list( point + _dir )
            if point + new_point in self.lines:
                if new_point in self.STACK:
                    return False
                else:
                    is_cycle( new_point )



    
    def stretch_lines(self):
    # before save to make it all nice and shine

        for i in xrange( len( self.lines ) ):
            self.lines[i] = list( array( self.lines[i] ) * self.side )
        return


    def draw_maze(self):
    # draws the maze

        self.stretch_lines()

        linewidth = str(self.side / 12.)
        im = svgwrite.drawing.Drawing()
        for i, line in enumerate( self.lines ):
            im.add( im.line(start  = line[:2],\
                            end    = line[2:],\
                            style  = 'stroke: black; stroke-width:'+ linewidth +';'))
            index = '_'+ str(i + 1).zfill( len( str( len( self.lines ))))

            #im.saveas('img/'+ self.filename + index +'.svg')
        im.saveas('img/static_'+ self.filename +'.svg')

        # convert svg files to gif
        #print ">>> converting to gif:"
        #gifname = str(size) +'_'+ type_path + put_path_to_string( path )
        #build   = 'convert -delay 72 img/braid_maze*.svg img/maze.gif'
        #os.system( build )
    
        # do the clean up
        #for f in sorted( [fn for fn in os.listdir('img/') if fn.startswith('braid_maze')]):  
        #    #print "--- {}".format( 'img/'+ f )
        #    os.remove( 'img/'+ f )    
        #return


if __name__ == '__main__':

    maze = BraidMazeOld(size=10, side=50)
    #maze.add_lines()
    maze.draw_maze()