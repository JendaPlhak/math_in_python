#!/usr/bin/env python
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy             as np

from random       import shuffle
from numpy        import dot, transpose
from numpy.linalg import inv
from clustering   import loadData
from math         import sqrt


def dataGenerator(n):

    x = np.arange(0, n)
    y = 5 - 2 * x + np.random.normal(0, 20, n)
    return zip(x, y)


def linearRegression(data):

    x_raw, y_raw = zip(*data)

    A = transpose(np.array([[1 for i in x_raw], x_raw]))
    y = transpose(np.array(y_raw))

    A_inv = dot( inv(dot(transpose(A), A)), transpose(A))

    return dot(A_inv, y)


def linearRegressionGradient(data):


    x_raw, y_raw = zip(*data)

    x = transpose(np.array([[1 for i in x_raw], x_raw]))
    y = transpose(np.array(y_raw))

    theta = np.array([0,0])
    alpha = 0.001

    for i in xrange(10000):
        error = dot(x, theta) - y
        delta = dot(transpose(x), error) / len(y_raw)**2
        theta = theta - alpha * delta

    return theta


def plotResult(l, data, path="linreg.png"):

    fig  = plt.figure(figsize=(23.5, 23.5))
    x, y = zip(*data)

    plt.plot(x, y, 'ro', markersize=8.)
    min_x = min(x)
    max_x = max(x)
    plt.plot([min_x, max_x], 
             [l[0] + min_x*l[1], l[0] + max_x*l[1]], 
             'k-')

    fig.savefig(path, dpi=80, bbox_inches='tight')


if __name__ == '__main__':

    data_pel = loadData("linreg.txt")
    line = linearRegression(data_pel)
    plotResult(line, data_pel, path="img/linreg.png")

    data = dataGenerator(1000)
    line = linearRegression(data)
    plotResult(line, data, path="img/linreg_random.png")
    print line
    
    line = linearRegressionGradient(data)
    plotResult(line, data, path="img/linreg_gradient.png")

    print line
   
