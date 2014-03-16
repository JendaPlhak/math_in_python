#!/usr/bin/env python
import sys
sys.path.append("../1_task")
from PIL     import Image
from spirals import coord_ArchimedSpiral
from math    import pi, tan



def elipse(a=100., b=200., size=500, path="img/circle.png", full=True, e=10):

    img = Image.new('RGB', (size,size), 'white')
    for x in xrange(size):
        for y in xrange(size):
            if full:
                if ((x - size/2) / a)**2 + ((y - size/2) / b)**2 <= 1:
                    img.putpixel( (x, y), (0,0,0))
            else:
                if ((x - size/2) / a)**2 + ((y - size/2) / b)**2 <= 1 and  \
                   ((x - size/2) / (a - e))**2 + ((y - size/2) / (b - e))**2 >= 1:
                    img.putpixel( (x, y), (0,0,0))
    img.save(path)


def archimedSpiral(size=500, path="img/spiral.png"):

    img = Image.new('RGB', (size,size), 'white')
    for length in xrange(35000):
        x, y = coord_ArchimedSpiral(length, pi/500)
        img.putpixel( (int(x) + size/2, int(y) + size/2), (0,0,0))
    img.show()
    img.save(path)

def triangle(a=200., size=500, path="img/triangle.png"):

    img = Image.new('RGB', (size,size), 'white')
    for x in xrange(-size/2, size/2):
        for y in xrange(size):
            if y <= tan(pi/3)*x + (a**2 - (a/2.)**2)**0.5 and y <= -tan(pi/3)*x + (a**2 - (a/2.)**2)**0.5:
                img.putpixel( (x + size/2, y + size/2), (int(x/float(size) * 255),  0, int(y/float(size) * 255)))
    img.save(path)


if __name__ == "__main__":

    elipse(full=False)
    archimedSpiral()
    triangle()