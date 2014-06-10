#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot  as plt

def fixed_points(last, r):

    fixed_points = []
    for i in range(1000):
        next = 4 * r * last * (1 - last)
        last = next
        if i > 500 and last not in fixed_points:
            fixed_points.append( last )

    return [ r ] * len(fixed_points), fixed_points


def bifurcation_diagram(last, x_axis=[0,1], r_axis=[0,1]):
    
    r_list   = []
    x_values = []

    # for thousand r from give interval
    for i in xrange(1,1000):
        # applying zoom on r_axis
        r = r_axis[0] + i * (r_axis[1] - r_axis[0]) / 1000.
        data = fixed_points(last, r)
        r_list.extend( data[0] )
        x_values.extend( data[1] )

    return r_list, x_values


def draw_bifurcation_diagram(last, x_axis=[0,1], r_axis=[0,1], save=False, filename='', box=[]):

    # get data for plot
    data = bifurcation_diagram(last, x_axis, r_axis)

    fig = plt.figure()
    plt.plot( data[0], data[1], 'ko', markersize=0.3)
    plt.ylim( x_axis )
    
    # adding zooming box
    if box:
            plt.plot( box[0], box[1], 'r-', linewidth=2)

    if save:
        fig.savefig( filename + '.png')


if __name__ == '__main__':

    # starting value for iteration
    start = 0.25

    box_1 = [ [0.7,0.95,0.95,0.7, 0.7], [0.3,0.3,0.9,0.9,0.3] ]
    draw_bifurcation_diagram(start, save=True, filename='feigenbaums_diagram_whole', box=box_1)

    box_2 = [ [0.85,0.9,0.9,0.85,0.85], [0.78,0.78,0.9,0.9,0.78]]
    draw_bifurcation_diagram(start, x_axis=box_1[1][1:3], r_axis=box_1[0][:2],\
                             save=True, filename='box_1', box=box_2)

    box_3 = [ [0.885,0.895,0.895,0.885,0.885], [0.87,0.87,0.9,0.9,0.87]]
    draw_bifurcation_diagram(start, x_axis=box_2[1][1:3], r_axis=box_2[0][:2],\
                             save=True, filename='box_2', box=box_3)

    draw_bifurcation_diagram(start, x_axis=box_3[1][1:3], r_axis=box_3[0][:2],\
                             save=True, filename='box_3')