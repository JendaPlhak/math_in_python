#!/usr/bin/env python

import matplotlib.pyplot as plt
matplotlib.use('Agg')
import numpy as np
import itertools
import re


def gcd_recursive_modulo(a, b):

    if a % b == 0:
        return b
    else:
        return gcd_modulo( b, a % b )


def gcd_modulo(a, b):

    steps = 0
    while a % b != 0:
        tmp = a
        a   = b
        b   = tmp % b

        steps +=1

    return steps


def gcd_substraction(a, b):

    a, b = max(a,b), min(a,b)
    
    steps = 0
    while a - b != 0:
        steps += 1
        a, b = max(b, a - b), min(b, a - b)
    return steps


def plot_gcd_algorithm(method, n=100, m=100, filename=''):

    # create zero matrix of given type n x m
    data = np.zeros((n, m))

    # fill it with steps or gcd
    for x, y in itertools.product(xrange(1, n + 1), xrange(1, m + 1)):
        data[x - 1][y - 1] = method(x, y)
    
    # plot the data, set origin to lb corner
    plt.imshow(data, interpolation='bilinear', origin='lower')
    # add colorbar
    plt.colorbar()
    # extract the name of the method
    name_method = re.sub(r'_', r' ', re.search(r'(\w+)_(\w+)', str(method)).group(0))
    # add title
    plt.title(name_method)

    # save or show
    if filename:
        plt.savefig(filename='img/'+ filename, format='png')
    else:
        plt.show()

    # finally clear the fig
    plt.clf()
    

def plot_fixed_par_gcd(fixed=7, method=gcd_modulo, n=100, filename=''):

    data = [range(1, n + 1),[]]
    for x in xrange(1, n + 1):
        data[1].append( method(fixed, x) )

    plt.plot(data[0], data[1], 'k-')

    # extract the name of the method
    name_method = re.sub(r'_', r' ', re.search(r'(\w+)_(\w+)', str(method)).group(0))
    # add title
    plt.title(name_method)

    # save or show
    if filename:
        plt.savefig(filename='img/'+ filename, format='png')
    else:
        plt.show()
    plt.clf()


if __name__ == '__main__':

    plot_gcd_algorithm(gcd_substraction, n=200, m=200, filename='gcd_substraction')
    plot_gcd_algorithm(gcd_modulo, n=200, m=200, filename='gcd_modulo')
    plot_gcd_algorithm(gcd_recursive_modulo, n=200, m=200, filename='gcd_recursive_modulo')

    for fixed in [1, 13, 171, 3141]:
        plot_fixed_par_gcd(fixed=fixed, method=gcd_substraction,  filename='gcd_substraction_'+ str(fixed))
        plot_fixed_par_gcd(fixed=fixed, method=gcd_modulo,  filename='gcd_modulo_'+ str(fixed))
        plot_fixed_par_gcd(fixed=fixed, method=gcd_recursive_modulo,  filename='gcd_recursive_modulo_'+ str(fixed))