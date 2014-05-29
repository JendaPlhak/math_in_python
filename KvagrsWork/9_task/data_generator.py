#! usr/bin/python

import matplotlib.pyplot as plt
from numpy.random import *


def generate_data(n=100, f=False, distribution=randn, sigma=1, mu=0):

    
    x_values = range(n)

    if not f:
        f = lambda x: x

    data = [x_values, [f(x) + sigma**0.5 * distribution() + mu for x in range(n) ]]

    return data


def lists_to_pairs(data):

    pairs = [ [data[0][i], data[1][i]] for i in xrange(len(data[0])) ]

    return pairs


def pairs_to_lists(data):

    lists = [[],[]]
    for item in data:
        lists[0].append( item[0] )
        lists[1].append( item[1] )

    return lists
    

if __name__ == '__main__':

    #data = generate_data(100, lambda x: x**2 + x)
    #plt.plot( data[0], data[1], 'bo')
    #plt.show()
    #plt.clf()
    data = generate_data()
    plt.plot( data[0], data[1], 'bo')
    plt.show()
    plt.clf()