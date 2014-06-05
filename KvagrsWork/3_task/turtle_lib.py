import svgwrite
from math   import sin, cos, pi, sqrt, atan
from numpy  import array

class Turtle(object):

    def __init__(self, absolute=False):
        self.x        = 0                          # Turtle starts at [0,0]
        self.y        = 0
        self.phi      = 0                        # Starting angle
        self.pen      = True
        self.absolute = absolute
        self.lines    = []
        self.coords   = [ [self.x, self.y] ]

    def forward(self, d):

        phi = self.degToRad(self.phi)       # conversion
        n_x = self.x + d*cos(phi)           # Calculating new coordinates
        n_y = self.y + d*sin(phi)
        self.coords.append( [n_x, n_y] )

        if self.pen == True:                # Drawing lines
            self.lines.append([self.x, self.y, n_x, n_y])   # One line is #4 list with start coord. and end coord.
            if self.absolute == False:
                self.x = n_x
                self.y = n_y
        else:                               # Changing the starting positions
            if self.absolute == False:
                self.x = n_x
                self.y = n_y
        return

    def back(self, d):
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


    def degToRad(self,phi):          # Conversion function from degrees to radians
        r_phi = (phi * pi) / 180
        return r_phi


    def radToDeg(self, rad):
        deg = (rad * 180)/pi
        return deg


    def draw_object(self, filename):

        self.calculate_offset()
        im = svgwrite.drawing.Drawing()
        for x in range(len(self.lines)):
            A = (self.lines[x][0],self.lines[x][1])            # Different offsets, to make i clearer on web
            B = (self.lines[x][2],self.lines[x][3])
            im.add( im.line(    start = A,\
                                end   = B,\
                                stroke= 'black'))       

        im.saveas( 'img/'+ filename +'.svg')
        return

    def calculate_offset(self):

        #frame = abs(array( map(max, zip(*self.coords)) ) - \
        #            array( map(min, zip(*self.coords)) ))
        offset = array( 2 * map(min, zip(*self.coords)) )
        print offset
        for line in self.lines:
            #print line
            line -= offset
            #print line
            #print

        
        return 





if __name__ == '__main__':

    turtle = Turtle()
    turtle.forward(50)
    turtle.forward(50)
    turtle.forward(50)
    turtle.forward(50)
    #turtle.draw_object(filename='turtle_lib')
    
    turtle.calculate_offset()
    turtle.draw_object('turtle_lib')