#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy             as np

from numpy        import dot, transpose
from numpy.linalg import inv
from clustering   import loadData


def dataGenerator(n):

    np.random.seed(5)
    x = np.arange(0, n)
    y = 20 + 3 * x + np.random.normal(0, 10, n)
    return zip(x, y)



def linearRegression(data):

    x_raw, y_raw = zip(*data)

    A = transpose(np.array([[1 for i in x_raw], x_raw]))
    y = transpose(np.array(y_raw))

    A_inv = dot( inv(dot(transpose(A), A)), transpose(A))

    return dot(A_inv, y)


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

    # data = loadData("linreg.txt")
    data = dataGenerator(100)
    line = linearRegression(data)
    plotResult(line, data)
