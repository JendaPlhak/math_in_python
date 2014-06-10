#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys 
for i in xrange(1,11):
    sys.path.append('../'+ str(i) +'_task')

import os

from linear_regression     import load
from data_generator        import *
from segment_intersection  import dist
from pascals_triangle      import different_colors
from hide_and_seek         import download_file, PATH

import matplotlib.pyplot as plt

import random
import re

def nearest_center(centers, point):

    nearest = centers[0]
    for center in centers:
        if dist(center, point) < dist(nearest, point):
            nearest = center

    return centers.index( nearest )


def find_center(data, center):

    if not data:
        return center

    data = pairs_to_lists( data )

    x_co = sum( data[0] ) / len( data[0] )
    y_co = sum( data[1] ) / len( data[1] )

    center = [x_co, y_co]

    return center


def k_means(data, k):

    centers     = lists_to_pairs( generate_data( k ) )
    data        = lists_to_pairs( data )
    classes     = [ [] for i in xrange(k) ]
    tmp_class   = []
    all_centers = list(centers)
    iteration   = 0

    while tmp_class != classes:
        tmp_class = list(classes)
        classes   = [ [] for i in xrange(k) ]

        for point in data:
            classes[ nearest_center(centers, point) ].append( point )

        for i, center in enumerate(centers):
            centers[ i ] = find_center( classes[ i ], center )

        iteration += 1
        all_centers.extend( centers )

    return classes, all_centers


def plot_data_clustering(classes, centers, k, filename=''):

    colors = different_colors( k, real=True )

    for i in xrange(k):
        plt.plot( pairs_to_lists(classes[i])[0], pairs_to_lists(classes[i])[1],'o',
                  markersize=5,\
                  color=colors[i])
        tmp_centers = pairs_to_lists( centers[i::k] )

        plt.plot(tmp_centers[0], tmp_centers[1], '-s', color=colors[i])

    title = re.sub(r'_', ' ', filename).title()
    plt.title( title )

    if filename:
        plt.savefig('img/'+ filename +'.png')
    else:
        plt.show()

    plt.clf()
    plot_shifts(centers, k, colors, filename)
    
    return


def plot_shifts(centers, k, colors, filename=''):

    iteration = len( centers ) / k - 1
    for i in xrange(k):
        tmp_centers = centers[i::k]
        values = []
        for j in xrange( iteration ):
            values.append( dist(tmp_centers[j], tmp_centers[j + 1]) )
        plt.plot(range(iteration), values, '-s', color=colors[i])

    plt.title('Differences of centroids')
    plt.xlabel('iteration $'+ str(iteration) +'$')
    plt.ylabel('$\Delta C$')
    
    if filename:
        plt.savefig('img/'+ filename +'_shifts.png')
    else:
        plt.show()
    plt.clf()

    return


if __name__ == '__main__':

    download_file( PATH +'faithful.txt')
    k = 2
    data = load('faithful.txt')
    classes, centers = k_means(data, k)
    plot_data_clustering(classes, centers, k, filename='data_cluster_faithful')

    download_file( PATH +'linreg-mix.txt')        
    data = load('linreg-mix.txt')
    classes, centers = k_means(data, k)
    plot_data_clustering(classes, centers, k, filename='linreg-mix')


    download_file( PATH +'cluster_data.txt')
    k = 5
    data = load('cluster_data.txt')
    classes, centers = k_means(data, k)
    plot_data_clustering(classes, centers, k, filename='data_cluster')