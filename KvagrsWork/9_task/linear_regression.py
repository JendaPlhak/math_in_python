#!/usr/bin/env python
import sys
for i in xrange(1,11):
    sys.path.append('../'+ str(i) +'_task')

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import operator

from itertools      import product
from numpy          import array, transpose, dot
from numpy.linalg   import inv, pinv
from numpy.random   import *
from math           import pi, tan, atan
from data_generator import *
from hide_and_seek  import download_file, PATH


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


def mean(data):
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
    x_av  = mean(data[0])
    y_av  = mean(data[1])
    b     = y_av - a * x_av

    # stretch the line
    x_value = [min(data[0]) - 1, max(data[0]) + 1]
    line    = [ x_value, [a * x + b for x in x_value] ]


    print "Analytic solution: $y={}\cdot x + {}$".format(a, b)
    return line


def SSE_grid_search(data, filename):
# calculate possible a,b such y = ax + b
# and find the minimal SSE
    min_x = min( data[0] )
    max_x = max( data[0] )

    min_b = min( data[1] )
    max_b = max( data[1] )

    b_range = step_list(min_b, max_b, 5)
    a_range = range(-40,60,20)

    plt.plot(data[0], data[1],'ro')
    colors = [tuple(3 * [ x ]) for x in step_list(0.1,1., len(b_range) * len(a_range))]    
    lines  = []
    for a, b in product(a_range, b_range):
        lines.append([a,b,calculate_SSE(data, a, b)])

    lines.sort(key=operator.itemgetter(2))

    min_SSE_index = 0
    for i, line in enumerate(lines):
        if lines[min_SSE_index][2] > lines[i][2]:
            min_SSE_index = i
        plt.plot([min_x, max_x], map(lambda x: line[0]*x + line[1],[min_x, max_x]), color=colors[i])

    a = lines[min_SSE_index][0]
    b = lines[min_SSE_index][1]

    print "Grid search solution: $y={}\cdot x + {}$".format(a, b)
    
    if filename:
        plt.savefig('img/'+ filename +'.png')
    else:
        plt.show()

    plt.clf()

    return


def plot_regression(data, line, filename=''):

    plt.plot(data[0], data[1], 'ro')
    plt.plot(line[0], line[1], 'b-', linewidth=3)

    if filename:
        plt.savefig('img/'+ filename +'.png')
    else:
        plt.show()
    plt.clf()
    return


if __name__ == '__main__':

    download_file( PATH + 'linreg.txt')
    data = load('linreg.txt')

    line = SSE_asol(data)
    plot_regression(data, line, filename='analytic_solution_linregtxt')
    line = SSE_grid_search( data, filename='grid_search_linregtxt')


    a = -2
    b =  5
    for distr in [normal, lognormal]:
        print "Generated line $y = {}\cdot x + {}$ with {} distribution.".format(a, b, distr.__name__)
        data = linear_data(n=100,distribution=distr, L=-5, U=50, a=a,b=b, sigma=10)
    
        line = SSE_asol( data )
        plot_regression(data, line, filename='analytic_solution_'+str(distr.__name__))

        line = SSE_grid_search( data, filename='grid_search_'+str(distr.__name__))