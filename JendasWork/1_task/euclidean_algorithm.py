#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np


def gcd_recursive(a, b):

    if b == 0:
        return a, None
    return gcd_recursive(b, a%b)


def gcd_mod(a, b):

    s = 0
    while b:
        s += 1
        a, b = b, a%b
    return a, s


def gcd_subtraction(a, b):

    s = 0
    while a != b:
        s += 1
        if a > b:
            a = a - b
        else:
            b = b - a
    return a, s


def create_and_savefig(size, gcd_algorithm, path, steps = True):

    matrix = np.zeros([size, size])
    for i in xrange(1,size):
        for j in xrange(i,size):
            GCD, steps  = gcd_algorithm(j, i)
            if steps:
                matrix[i,j] = steps
                matrix[j,i] = steps 
            else:
                matrix[i,j] = GCD
                matrix[j,i] = GCD
    plt.figure(1,figsize=(10, 10))
    plt.imshow(matrix, interpolation='nearest')
    plt.colorbar()
    plt.suptitle(path[:-4].replace("_", " "))
    plt.savefig(path)
    plt.clf()



size = 51
create_and_savefig(size, gcd_recursive,   "gcd_recursive.png", steps = False)

size = 501
create_and_savefig(size, gcd_mod,         "gcd_modulo_steps.png")
create_and_savefig(size, gcd_subtraction, "gcd_subtraction_steps.png")