#! usr/bin/python

import matplotlib.pyplot as plt
import itertools
from numpy          import array, transpose, dot
from numpy.linalg   import inv, pinv
from numpy.random   import *
from math           import pi, tan, atan
from data_generator import generate_data


def load(filename):

    with open( filename , 'r') as f:
        data = [[],[]]
        for line in f:
            x, y = [float(x) for x in line.split()]
            data[0].append( x )
            data[1].append( y )
            
    return data


def step_list(a, b, n):
    return [a + i * (b - a) / (n - 1) for i in range(n)]


def average(data):
    return sum(data) / len(data)

def plot_data(data):
    plt.plot(data[0], data[1], 'ro')
    return


def plot_line(line, style='-'):
    plt.plot( line[0], line[1], style)
    return


def calculate_SSE(data, a, b):
    # returns the SSE
    return sum([(a * data[0][i] + b - data[1][i])**2 for i in range(len(data[0]))])


def SSE_asol(data):
    # find y = ax + b

    n     = len( data[0])

    # calculating coeff a 
    numer = n * sum( [data[0][i]*data[1][i] for i in xrange(n)] ) - sum(data[0])*sum(data[1])
    denom = n * sum( [x**2 for x in data[0]] ) - sum(data[0])**2
    a     = numer / denom

    # calculating coeff b
    x_av  = average(data[0])
    y_av  = average(data[1])
    b     = y_av - a * x_av

    # stretch the line
    x_value = [min(data[0]) - 1, max(data[0]) + 1]
    line    = [ x_value, [a * x + b for x in x_value] ]

    return line


def MP_pseudoinverse(data):

    pass

def SSE_grid_search(data, nb, na):
    # calculate possible a,b such y = ax + b
    # and find the minimal SSE

    min_a = (min(data[1]) / min(filter(None, data[0])))
    max_a = (max(data[1]) / max(filter(None, data[0])))

    # create the grid
    a_list  = map(tan, step_list(min_a, max_a, na))
    b_list  = step_list(min(data[1]), max(data[1]), nb)
    near_a  = a_list[0]
    near_b  = b_list[0]
    min_SSE = calculate_SSE(data, near_a, near_b)

    x_av    = average(data[0])
    for a, b in itertools.product( a_list, b_list ):
        plt.plot([-1, 1], [-a + b, a + b], 'g-')
        if min_SSE > calculate_SSE(data, a, b):
            near_a, near_b = a, b
            min_SSE        = calculate_SSE(data, a, b)
    plt.show()
    # stretch the line
    x_value = [min(data[0]) - 1, max(data[0]) + 1]
    line    = [ x_value, [near_a * x + near_b for x in x_value] ]
    return line



if __name__ == '__main__':


    data = generate_data(lambda x: -3*x-2, 100, distribution=randn, sigma=10)

    #plot_data( data )
    plot_line( SSE_grid_search( data, 2, 10 ), 'b-')
    #plot_line( SSE_asol( data ), 'g-' )
    #plt.show()
    #print step_list(-10, 20, 3)

    #tro = map(tan, step_list(0,pi, 10))
    #for i in range(10):
    #    for t in tro[:8]:
    #        print t
    #        plt.plot([-1,1], [-t+i, t+i],'k-')
    #plt.show()