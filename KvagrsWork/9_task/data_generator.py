#!/usr/bin/python
import sys
sys.path.append('../2_task')
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

from numpy.random     import *
from numpy            import array
from pascals_triangle import different_colors


def generate_data(n=100, f=False, distribution=randn, sigma=1, mu=0):

    x_values = range(n)

    if not f:
        f = lambda x: x

    data = [x_values, [f(x) + sigma**0.5 * distribution() + mu for x in range(n) ]]

    return data


def linear_data(n=100, distribution=normal, a=1, b=0, L=0, U=1, mean=1, sigma=1):
# distribution: normal, lognormal
    x_range = [ uniform(L, U) for i in xrange(n) ]
    data    = [ x_range ]
    data.append( [ a*x + b + distribution(mean, sigma) for x in x_range ] )
    
    return data


def cluster_data(k=4, n=100, U=0, L=100, centroids=[], dif=2):

    data = []
    if not centroids:
        centroids = []
        for i in xrange(k):
            centroids.append( [uniform(U, L), uniform(U, L)] )

    #k = len(centroids)
    nums = []
    for i in xrange(k - 1):
        nums.append( n / k + randint( -n / k**2, n / k**2 ) )
    nums.append( n - sum(nums) )

    for i, centroid in enumerate(centroids):
        for j in xrange(nums[i]):

            point = centroid + array([uniform(-dif / 2, dif / 2), uniform(-dif / 2, dif / 2)])
            data.append( point )

    data = pairs_to_lists( data )

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

def plot_linear_data(data, filename=''):

    pass

def plot_dataset(dataset, filename=''):

    colors = different_colors( len(dataset), real=True )
    for i, data in enumerate(dataset):
        plt.plot(data[0], data[1], 'o', color=colors[i])

    if filename:
        plt.savefig('img/'+ filename +'.png')
    else:
        plt.show()

    plt.clf()
    return
    

if __name__ == '__main__':

    #dataset = [ linear_data(distribution=lognormal, b=50, sigma=10) ]
    #dataset.append( linear_data(distribution=normal,b=50, sigma=10))
    #dataset.append( linear_data(distribution=logistic,b=50, sigma=10))
    #dataset.append( linear_data(distribution=laplace,b=50, sigma=10))
    #plot_dataset( dataset )
    #centroids = lists_to_pairs( generate_data(n=5) )
    #print cluster_data(k=5, centroids=centroids, dif=10)
    dataset   = [ cluster_data(L=2, dif=0.3) ]
    plot_dataset( dataset, 'random_cluster' )
    dataset = [ linear_data(U=5) ]
    plot_dataset( dataset, 'random_linear')