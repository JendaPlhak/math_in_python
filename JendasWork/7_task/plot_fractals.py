#!/usr/bin/env python

from complex_frac import complexFractal

if __name__ == '__main__':

    complexFractal(julia_=True,  path="img/Julia_Set.png")
    complexFractal(julia_=False, path="img/Mandelbrot_set.png")