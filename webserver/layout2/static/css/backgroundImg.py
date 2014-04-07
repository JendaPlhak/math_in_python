import svgwrite
from random import randint
#import itertools

def drawBackgroundImage():

    draw = svgwrite.drawing.Drawing(fill="#222266")
    side = 25
    
    for i in xrange(10):
        for j in xrange(10):
            for k in xrange(5):
                x   = randint(0,50) * side + i * side
                y   = randint(0,50) * side + i * side

                pos = (x, y)
                opac = 100./randint(180,220)
                draw.add( draw.rect( insert = pos,\
                                     size   = (side, side),\
                                     rx     = (5),\
                                     ry     = (5),\
                                     fill   = "#225588",\
                                     opacity= opac
                                     ))
    
    draw.saveas('backgroundImage.png')

if __name__ == '__main__':

    drawBackgroundImage()