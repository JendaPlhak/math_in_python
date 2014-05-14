#!/usr/bin/env python
import sys
sys.path.append("../3_task")

import math
import numpy as np
from Turtle import Turtle

norm  = np.linalg.norm
acos  = math.acos
dot   = np.dot


def clean_cos(cos_angle):
    return min(1.,max(cos_angle,-1.))


def findLeftmost(points):

    leftmost = np.array([float("inf"), float("inf")])
    for i, point in enumerate(points):
        if point[0] < leftmost[0]:
            leftmost = point
            index    = i
    return points.pop(index)


def wrapGift(points):

    leftmost = findLeftmost(points)
    wraping  = [np.array([leftmost[0], leftmost[1] + 100])]
    first    = True

    while not (leftmost == wraping[0]).all():
        V = wraping[-1] - leftmost
        max_value = float("-inf")

        for i, point in enumerate(points):
            L_P     = point - leftmost
            cos_val = clean_cos(dot(L_P, V) / (norm(L_P)*norm(V)))
            angle   = acos(cos_val)

            if angle > max_value:   # We want to maximize the angle
                max_value = angle
                index     = i

        wraping.append(leftmost)
        leftmost = points.pop(index)

        if first:
            wraping.pop(0)                 # remove initial point
            points.insert(0, wraping[0])   # Insert the first point back to points so we can end.
            first = False
    else:
        wraping.append(leftmost)
    return wraping




def wrapRandomGift(n, uniform=True):

    if uniform:
        draw   = Turtle("Gift_Wraping_uniform")
        points = list(np.random.uniform(0,750,[n,2]))
    else:
        draw   = Turtle("Gift_Wraping_normal")
        mean, sigma = 200, 70
        points = list(np.random.normal(mean,sigma,[n,2]))

    for point in points:
        draw.addPoint(point)

    while len(points) >= 3:
        wraping = wrapGift(points)
        wr_len  = len(wraping)
        for i in xrange(wr_len):
            draw.addLineNumpy(wraping[i], wraping[(i+1) % wr_len])

    draw.dumpImage()


if __name__ == '__main__':
    wrapRandomGift(50)
    wrapRandomGift(100, False)