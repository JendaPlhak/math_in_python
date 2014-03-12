import numpy as np
from libc.stdlib cimport malloc, free


cdef struct Complex:
    
    float re
    float im


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


def juliaFractal(width=500, height=500,c_num=0.285+0.01*1j, path="trol.png"):
     
    # Specify image width and height
    cdef int w = width
    cdef int h = height
    cdef int i
     
    # Specify real and imaginary range of image
    re_min, re_max = -1., 1.
    im_min, im_max = -1, 1.
     
    # Pick a value for c
    cdef Complex c
    c.re = c_num.real
    c.im = c_num.imag

    
    cdef int **output = <int **> malloc(sizeof(int *) * w)
    for i in xrange(w):
        output[i] = <int *> malloc(sizeof(int) * h)


    # Open output file and write PGM header info
    fout = open('trol.pgm', 'w')
    fout.write('P2\n# Julia Set image\n' + str(w) + ' ' + str(h) + '\n255\n')
     
    # Generate pixel values and write to file
    cdef float step_x = abs(re_max - re_min) / w
    cdef float step_y = abs(im_min - im_max) / h

    cdef int n, x, y
    cdef Complex z

    for x in xrange(w):
        for y in xrange(h):
            z.re = re_min + x*step_x
            z.im = im_min + y*step_y
            n = 255
            while z.re**2 + z.im**2 < 10 ** 2 and n >= 5:
                z = cAdd(cMultiply(z, z), c)
                n -= 1
            output[x][y] = n
    
    print "Calculation finished!"
    
    # Write pixels to file
    for x in xrange(w):
        for y in xrange(h):
            fout.write(str(output[x][y]) + ' ')
        fout.write('\n')
    fout.close()


    # Clean up
    for i in xrange(w):
        free(output[i])
    free(output)


def mandelbrot():
    pass
