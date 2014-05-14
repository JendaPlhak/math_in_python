#!/usr/bin/env python
import sys
sys.path.append("../3_task")

import numpy as np
import math, random
from Turtle       import Turtle
from intersection import segmentIntersect

norm = np.linalg.norm

class Edge():

    def __init__(self, A, B):
        self.A     = A
        self.B     = B
        self.array = np.row_stack((A,B))
        self.norm  = norm(B-A)


def sharePoint(A, B):
    for i in xrange(2):
        for j in xrange(2):
            if (A[i] == B[j]).all():
                return True
    return False


def triangulation(points):    # Greedy algorithm

    n = len(points)
    edges = []
    for i, point1 in enumerate(points):
        for point2 in points[i+1:,:]:
            edges.append(Edge(point1, point2))
    edges.sort(key=lambda edge: edge.norm)

    edges_triang = []

    for edgeNew in edges:
        add = True
        for edge in edges_triang:
            inSec = segmentIntersect(edgeNew.array, edge.array)
            if not sharePoint(edgeNew.array, edge.array) and inSec != None:
                add = False
                break
        if add:
            edges_triang.append(edgeNew)
            
    return edges_triang




def triangulateRandom(n, uniform=True):

    if uniform:
        points = np.random.uniform(0,700,[n,2])
        draw   = Turtle("triangulation_uniform_points")
    else:
        mean, sigma = 200, 70
        points = np.random.normal(mean,sigma,[n,2])
        draw   = Turtle("triangulation_normal_points")

    for edge in triangulation(points):
        draw.addLineNumpy(edge.array[0,:], edge.array[1,:])
    draw.dumpImage()


if __name__ == '__main__':
    triangulateRandom(30)
    triangulateRandom(50, False)
