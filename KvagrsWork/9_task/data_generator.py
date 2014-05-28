#! usr/bin/python

import matplotlib.pyplot as plt
from numpy.random import *


def generate_data(n=100, f=False, distribution=randn, sigma=1, mu=0):

    if f:
        x_values = range(n)
    else:
        x_values = [f(x) + sigma**0.5 * distribution() + mu for x in range(n) ]
        
    data = [x_values, [f(x) + sigma**0.5 * distribution() + mu for x in range(n) ]]

    return data


if __name__ == '__main__':

    #data = generate_data(100, lambda x: x**2 + x)
    #plt.plot( data[0], data[1], 'bo')
    #plt.show()
    #plt.clf()
    data = generate_data()
    plt.plot( data[0], data[1], 'bo')
    plt.show()
    plt.clf()