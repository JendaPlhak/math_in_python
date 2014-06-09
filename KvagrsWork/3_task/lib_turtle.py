#!/usr/bin/env python

import os
import svgwrite
import cairo
import rsvg
#import wand

from math       import sin, cos, pi, sqrt, atan, atan2
from numpy      import array
from images2gif import writeGif
from PIL        import Image


class Turtle(object):

    def __init__(self, absolute=False):
        # Turtle starts at [0,0]
        self.x        = 0
        self.y        = 0
        # Starting angle
        self.phi      = 0
        self.pen      = True
        self.absolute = absolute
        self.lines    = []
        self.dots     = []
        self.coords   = [ [self.x, self.y] ]

    def line(self, coords):

        self.coords.extend( [ coords[:2], coords[2:] ] )
        self.lines.append( coords )
        return


    def forward(self, d):

        # conversion
        phi = radians(self.phi)
        # calculating new coordinates
        n_x = self.x + d*cos(phi)
        n_y = self.y + d*sin(phi)
        self.coords.append( [n_x, n_y] )

        # drawing lines
        if self.pen == True:
            # one line is 4-list with start coord. and end coord.
            self.lines.append( array( [self.x, self.y, n_x, n_y] ) )
            if self.absolute == False:
                self.x = n_x
                self.y = n_y
        # Changing the starting positions
        else:
            if self.absolute == False:
                self.x = n_x
                self.y = n_y
        return

    def back(self, d):
        # go forward with negative distance
        self.forward(-d)
        return


    def left(self, phi):
        self.phi -= phi
        return


    def right(self, phi):
        self.phi += phi
        return


    def penup(self):
        self.pen = False
        return


    def pendown(self):
        self.pen = True
        return

    def start(self):
        self.x = 0
        self.y = 0
        return

    def dot(self, pos, radius=5, color='blue'):

        self.dots.append( pos )
        return

    def restart(self, absolute=False):

        self.x        = 0
        self.y        = 0
        self.phi      = 0
        self.pen      = True
        self.absolute = absolute
        self.lines    = []
        self.dots     = []
        self.coords   = [ [self.x, self.y] ]

        return


    def reset(self):

        self.x   = 0
        self.y   = 0
        self.phi = 0
        self.pen = True

        return


    def set_pos(self, pos):

        self.x = pos[0]
        self.y = pos[1]

        return

    def set_dir(self, _dir):

        self.phi = _dir

        return

    def draw_object(self, filename='', gif=False):

        self.calculate_offset()
        im = svgwrite.drawing.Drawing()
        if gif:
            print "Creating files:"

        for x in range( len(self.lines) ):
            A = ( self.lines[x][:2]) 
            B = ( self.lines[x][2:])
            im.add( im.line(start = A,\
                            end   = B,\
                            stroke= 'black'))
            if gif:
                self.generate_png(im, x)

        if self.dots:
            for dot in self.dots:
                im.add( im.circle(center = dot,\
                                  r      = 5,\
                                  fill   = 'blue'))  
        if filename:
            im.saveas( 'img/'+ filename +'.svg')
            if gif:
                self.gifit( filename )
                self.clear_png( len(self.lines) )
        return


    def calculate_offset(self):

        # calculates the minimal coordinate
        offset = array( 2 * map(min, zip(*self.coords)) )
        # shifts each line by offset        
        for i in xrange(len(self.lines)):
            self.lines[i] -= offset

        for i in xrange(len(self.dots)):
            self.dots[i] -= offset[:2]

        return 


    def gif_frame(self):

        mins = array( map( lambda x: int(x), 2 * map(min, zip(*self.coords)) ))
        maxs = array( map( lambda x: int(x), 2 * map(max, zip(*self.coords)) ))
        frame = maxs - mins + array([1, 1, 0 ,0])

        return frame


    def generate_png(self, im, index):

        frame = self.gif_frame()
        img   = cairo.ImageSurface(cairo.FORMAT_ARGB32, frame[0], frame[1])
        ctx   = cairo.Context(img)
        
        ## handler= rsvg.Handle(<svg filename>)
        # or, for in memory SVG data:
        #with open('example_star_even_16.svg','r') as f:
        #   svg_data = f.read()
        svg_data = im.tostring()
        #print svg_data
        handler  = rsvg.Handle(None, str(svg_data))
        handler.render_cairo(ctx)

        #if index < 9:
        ## adding necessary zero for sorting the pictures for imageMagick
        #    path = 'img/gif_part_0' + str(index + 1)
        #else:
        #    path = 'img/gif_part_'
        path  = 'img/gif_part_'
        path += str(index + 1).zfill( len( str( len( self.lines ))))
        print "+++ {}.png".format( path )

        img.write_to_png( path +'.png')
        return

    def clear_png(self, index):

        #for i in range( index ):
        print "Removing files: "
        for f in [fn for fn in os.listdir('img/') if fn.startswith('gif_part_')]:   
            print "--- {}".format( 'img/'+ f )
            os.remove( 'img/'+ f )

        return


    def gifit(self, filename):

        build   = 'convert -delay 16 img/gif_part_*.png img/'+ filename +'.gif'
        if not os.system( build ):
            print "Succesfully converted.. {}.gif".format( filename )

        return


def radians(phi):
# conversion function from degrees to radians

    r_phi = (phi * pi) / 180.
    return r_phi


def degrees(rad):
# conversion function from radians to degrees

    deg = (rad * 180.) / pi
    return deg


def polygon(turtle, side, n=5):

    for x in range(n):
        turtle.forward( side )
        turtle.left(360. / n)

    return


def star(turtle, side, n=9):

    if n % 2 == 1:
        for x in range( n ):
            turtle.forward( side )
            turtle.left( (n + 1) / 2 * 360. / n )
    else:
        angle = degrees( atan2( 1, 2) )
        side  = ( side**2 + (side / 2.)**2 )**0.5

        for i in range( n ):
            turtle.left( angle )
            turtle.forward( side )
            turtle.right( 2 * angle )
            turtle.forward( side )
            turtle.left( 360. / n + angle)

    return


if __name__ == '__main__':

    
    print "Creating examples of the lib_turtle.."

    turtle = Turtle()
    """ 
    polygon(turtle, 100, 6)
    turtle.draw_object('example_polygon')
    turtle.restart()

    for i in [5, 17, 51]:
        star(turtle, 100, i)
        turtle.draw_object('example_star_odd_'+ str(i))
        turtle.restart()

    for i in [4, 16, 42]:
        star(turtle, 10, i)
        turtle.draw_object('example_star_even_'+ str(i))
        turtle.restart()

    """
    #star(turtle, 100, 5)
    #turtle.draw_object('test')
    polygon(turtle, 100, 3)
    turtle.draw_object('dvojuhelnik', gif=True)