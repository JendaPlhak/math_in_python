#! usr/bin/env python
import sys 
for i in xrange(1,11):
    sys.path.append('../'+ str(i) +'_task')

from linear_regression      import load
from data_generator         import *
from segment_intersection   import dist

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

    #print "moving {} to {}".format( center, [x_co, y_co])
    center = [x_co, y_co]
    #print center
    return center


def k_means(data, k):

    centers   = lists_to_pairs( generate_data( k ) )
    data      = lists_to_pairs( data )
    classes   = [ [] for i in xrange(k) ]
    tmp_class = []

    plt.plot( pairs_to_lists(centers)[0], pairs_to_lists(centers)[1], 'ro') 

    while tmp_class != classes:
        print "Centers: {}".format(centers)
        print "tmp_class == classes is {}".format(tmp_class == classes)
        tmp_class = list(classes)
        classes   = [ [] for i in xrange(k) ]

        for point in data:
            classes[ nearest_center(centers, point) ].append( point )

        for i, center in enumerate(centers):
            print "center : {}".format(center)
            center = find_center( classes[ i ], center )
            plt.plot(center[0], center[1], 'go')
            print "moved  : {}".format(center)
    
    print "tmp_class == classes is {}".format(tmp_class == classes)
    #plt.plot( pairs_to_lists(centers)[0], pairs_to_lists(centers)[1], 'bo')        
    plt.plot( pairs_to_lists(data)[0], pairs_to_lists(data)[1], 'ko')
    plt.show()
    
    return


if __name__ == '__main__':

    data = load('data_cluster.txt')
    k_means(data, 5)
    #print [[1,2],[2,4],[3,4]] == 
    #centers = [[1,2],[2,4],[3,4]]
    #point = [2,2]
    #print centers[ nearest_center( centers, point)]