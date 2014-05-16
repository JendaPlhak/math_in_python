#!/usr/bin/env python

from complex_frac import complexFractal

if __name__ == '__main__':

    # complexFractal(julia_=True,  path="img/Julia_Set.png")
    # complexFractal(julia_=False, path="img/Mandelbrot_set.png")
    complexFractal(newton=1, path="img/Newton_method1.png")
    complexFractal(newton=2, path="img/Newton_method2.png")
    complexFractal(newton=3, path="img/Newton_method3.png")
    complexFractal(newton=4, path="img/Newton_method4.png")