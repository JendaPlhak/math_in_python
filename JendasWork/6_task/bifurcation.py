#!/usr/bin/env python

from PIL import Image


def bifurcation(path):

    s_x   = 1000
    s_y   = 500
    img = Image.new("RGB", (s_x, s_y), "white")

    n_iter = 700

    x_a    = 2.5
    x_b    = 4.

    y_a    = 0.1
    y_b    = 0.9

    for i in xrange(s_x):
        r = x_a + (x_b - x_a) * i / float(s_x - 1)
        x = 0.5
        for j in xrange(n_iter):
            x = r * x * (1 - x)
            if j > n_iter / 3:
                if x > y_a and x < y_b:
                    q = 1 / (y_b - y_a)
                    y = int( (x - y_a) * q * s_y )
                    img.putpixel((i, y), (100, 0, 200))

    img.save(path, "png")


if __name__ == '__main__':
    
    bifurcation("img/Bifurcation.png")
