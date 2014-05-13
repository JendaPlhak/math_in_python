#!/usr/bin/env python
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

    a = 0
    b = 0
    n = 0
    while n <= 10:
        n += 1
        shuffle(data)
        for x, y in data:
            grad_a = 2*(a*x + b - y) * x
            grad_b = 2*(a*x + b - y)

            norm = sqrt(grad_a**2 + grad_b**2)
            a -= grad_a / norm
            b -= grad_b / norm

    return [b, a]


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

    data = dataGenerator(100)
    line = linearRegression(data)
    plotResult(line, data, path="img/linreg_random.png")
    print line
    
    line = linearRegressionGradient(data)
    plotResult(line, data, path="img/linreg_gradient.png")

    print line
   
