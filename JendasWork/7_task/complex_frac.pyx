#!/usr/bin/env python
import numpy as np
import colorsys

from PIL import Image
from libc.stdlib cimport malloc, free, pow
cimport cython


cdef struct Complex:
    
    double re
    double im


cdef inline Complex cMultiply(Complex a, Complex b):
    
    cdef Complex result

    result.re = a.re * b.re - a.im * b.im
    result.im = a.re * b.im + a.im * b.re
    return result


cdef inline Complex cAdd(Complex a, Complex b):
    
    cdef Complex result

    result.re = a.re + b.re
    result.im = a.im + b.im 
    return result

cdef inline Complex cDiff(Complex a, Complex b):
    
    cdef Complex result

    result.re = a.re - b.re
    result.im = a.im - b.im 
    return result


@cython.cdivision(True)
cdef inline Complex cDiv(Complex a, Complex b):
    
    cdef Complex result
    result.re  = a.re * b.re + a.im * b.im
    result.im  = a.im * b.re - a.re * b.im

    result.re /= b.re**2 + b.im**2
    result.im /= b.re**2 + b.im**2

    return result


cdef inline double cAbs(Complex a):
    return a.re * a.re + a.im * a.im


cdef inline Complex cNewNumber( double re_min, double im_min, 
                                double step_x, double step_y,
                                int x, int y):
    cdef Complex result
    result.re = re_min + x*step_x
    result.im = im_min + y*step_y
    return result

cdef inline Complex cPow(Complex z, int n):

    cdef int i
    cdef Complex result = z
    for i in xrange(n - 1):
        result = cMultiply(result, z)  
    return result

ctypedef Complex (*cFun_t)(Complex)

cdef inline Complex cFun1(Complex z):
    
    cdef Complex i
    i.re = 1
    i.im = 0
    return cDiff(cPow(z,3), i)

cdef inline Complex cFun2(Complex z):
    
    cdef Complex i
    i.re = 1
    i.im = 0
    return cDiff(cPow(z,7), i)

cdef inline Complex cFun3(Complex z):
    
    cdef Complex i
    i.re = 1
    i.im = 0
    return cAdd(cPow(z,3), cDiff(cPow(z,7), i))

cdef inline Complex cFun4(Complex z):
    
    cdef Complex i, result
    i.re = 13
    i.im = 0
    result = cDiff(cPow(z,7), i)

    i.re   = 3
    return cAdd(result, cMultiply(cPow(z,4), i))


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def complexFractal(width=3000, height=2000,c_num=-0.8+0.156*1j, julia_=True, newton=0, path="img/trol.png"):
     
    # Specify image width and height
    cdef int w = width
    cdef int h = height
    cdef int i
    cdef int julia    = int(julia_)
    cdef int treshold = 2 if julia else 50
    shift = 0.
    zoom  = 10. if julia else 1.
    # Specify real and imaginary range of image
    re_min, re_max = -2*(1/zoom) + shift, 1*(1/zoom) + shift
    im_min, im_max = -1*(1/zoom) + shift, 1*(1/zoom) + shift
    # Pick a value for c
    cdef Complex c
    c.re = c_num.real
    c.im = c_num.imag

    cdef int **output = <int **> malloc(sizeof(int *) * w)
    for i in xrange(w):
        output[i] = <int *> malloc(sizeof(int) * h)

    # Generate pixel values and write to file
    cdef double step_x = abs(re_max - re_min) / w
    cdef double step_y = abs(im_min - im_max) / h

    cdef int n, x, y
    cdef Complex z, zero, t, dz, z0
    cdef cFun_t cFun


    t.re = 1e-3
    t.im = 1e-3
    zero.re = 0
    zero.im = 0

    if not newton:
        for x in xrange(w):
            for y in xrange(h):
                if julia:
                    z = cNewNumber(re_min, im_min, step_x, step_y, x, y)
                else:
                    z = zero
                    c = cNewNumber(re_min, im_min, step_x, step_y, x, y)
                n = 255
                while z.re**2 + z.im**2 < treshold**2 and n >= 1:
                    z  = cAdd(cMultiply(z, z), c)
                    n -= 1
                output[x][y] = n
    else:
        #Calculate Newtons Fractal
        if newton == 1:
            cFun = cFun1
        elif newton == 2:
            cFun = cFun2
        elif newton == 3:
            cFun = cFun3
        elif newton == 4:
            cFun = cFun4
        for x in xrange(w):
            for y in xrange(h):
                z = cNewNumber(re_min, im_min, step_x, step_y, x, y)
                for n in xrange(100):
                    cAdd(z, t)
                    cFun(z)
                    dz = cDiff(cFun(cAdd(z, t)), cFun(z))
                    dz = cDiv(dz, t)
                    z0 = cDiff(z, cDiv(cFun(z), dz))
                    if cAbs(cDiff(z0, z)) < 1e-3 * 1e-3:
                        break
                    z = z0
                output[x][y] = n
    
    print "Fractal generated!"
    

    col_n = 75
    HSV_tuples = [(j*1.0/col_n, 0.85, 0.85) for j in xrange(col_n)]
    RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
    RGB_tuples = [tuple([int(j * 255) for j in colour]) for colour in RGB_tuples]

    img     = Image.new( 'RGB', (w,h))
    pix_map = img.load()

    # Write pixels to file
    for x in xrange(w):
        for y in xrange(h):
            pix_map[x, y] = RGB_tuples[output[x][y] % col_n]
    img.save(path)

    # Clean up
    for i in xrange(w):
        free(output[i])
    free(output)
    print "Fractal printed!"
