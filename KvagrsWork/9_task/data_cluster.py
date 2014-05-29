#! usr/bin/env python
import sys 
for i in xrange(1,11):
    sys.path.append('../'+ str(i) +'_task')

from linear_regression      import load
from data_generator         import *
from segment_intersection   import dist
from pascals_triangle       import different_colors
import matplotlib.pyplot as plt

import random


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


def k_means(data, k, filename=''):

    centers     = lists_to_pairs( generate_data( k ) )
    data        = lists_to_pairs( data )
    classes     = [ [] for i in xrange(k) ]
    tmp_class   = []
    all_centers = list(centers)

    while tmp_class != classes:
        tmp_class = list(classes)
        classes   = [ [] for i in xrange(k) ]

        for point in data:
            classes[ nearest_center(centers, point) ].append( point )

        for i, center in enumerate(centers):
            centers[ i ] = find_center( classes[ i ], center )

        all_centers.extend( centers )

    colors = different_colors( k, real=True )

    for i in xrange( k ):
        plt.plot( pairs_to_lists(classes[i])[0], pairs_to_lists(classes[i])[1], 'o', color=colors[i],)
        plt.plot( centers[i][0], centers[i][1], 's', color=colors[i], markersize=10)

    if filename:
        plt.savefig('img/'+ filename, format='png')
    else:
        plt.show()
    plt.clf()
    
    return


if __name__ == '__main__':

    data = load('faithful.txt')
    k_means(data, k=2, filename='data_cluster_faithful')

    #data = load('data_cluster.txt')
    #k_means(data, k=5, filename='data_cluster')