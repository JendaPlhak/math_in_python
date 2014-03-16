#!/usr/bin/env python
import itertools
from PIL  import Image
from math import pi, sin, cos


def waves(A=500, a=200, path="img/Waves.png"):

    img   = Image.new('RGB', (A,A), 'white')
    shift = A/2
    for x, y in itertools.product(xrange(-A/2, A/2), xrange(-A/2, A/2)):
        coef = abs( sin( ((x/5.)**2 + (y/5.)**2)**0.5 ))

        if abs(x) <= a/2 and abs(y) < a/2:
            coef = 1 - coef

        img.putpixel( (x + shift, y + shift), tuple([int(255 * coef)] * 3))
    img.save(path)


def compositeImage(size=500, path="img/CompositeImage.png"):

    img = Image.new('RGB', (size,size))

    for x, y in itertools.product(xrange(size), xrange(size)):
        r = int( 255*max(0, sin(x/5.)         ))
        g = int( 255*max(0, sin(y/5.)         ))
        b = int( 255*max(0, sin(x/10. + y/10.)))
        img.putpixel((x, y), (r, g, b))

    img.save(path)




if __name__ == '__main__':
    waves()
    compositeImage()