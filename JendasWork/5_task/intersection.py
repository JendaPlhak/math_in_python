#!/usr/bin/env python
import sys
sys.path.append("../3_task")

import numpy as np
import math, random
from Turtle import Turtle

det  = np.linalg.det
norm = np.linalg.norm

def sameNorm(A, B, P):
    return norm(A - P) + norm(B - P) - norm(A - B) < 0.001


def segmentIntersect(seg_1, seg_2):  # Following determinant algorithm from http://en.wikipedia.org/wiki/Line_intersection

    #       | det1 det3 |  numerator X
    #       | det2 det4 |

    #       | det1 det5 |  numerator Y
    #       | det2 det6 |

    #       | det3 det5 |  denominator DENOM
    #       | det4 det6 |

    one_col = np.array([[1], [1]])

    det1 = det(seg_1)
    det2 = det(seg_2)

    det3 = det(np.column_stack((seg_1[:,0], one_col)))
    det4 = det(np.column_stack((seg_2[:,0], one_col)))
    det5 = det(np.column_stack((seg_1[:,1], one_col)))
    det6 = det(np.column_stack((seg_2[:,1], one_col)))

    DENOM = det(np.array([[det3, det5], [det4, det6]]))
    if DENOM == 0:
        return None

    P_X = det(np.array([[det1, det3], [det2, det4]])) / DENOM
    P_Y = det(np.array([[det1, det5], [det2, det6]])) / DENOM

    P = np.array([[P_X, P_Y]])

    # Norm has to be the same.
    if sameNorm(seg_1[0,:], seg_1[1,:], P) and sameNorm(seg_2[0,:], seg_2[1,:], P):
        return P
    else:
        return None


def randomVector(l):

    angle = random.uniform(0., 2*math.pi)
    cos   = math.cos(angle)
    sin   = math.sin(angle)
    x = l*cos
    y = l*sin
    return np.array([[x, y]])


def randomSegments(n, l=150):

    points = np.random.uniform(0,300,[n,2])
    vector = np.array([[l, 0]])
    pairs  = []
    for i in xrange(n):
        A = points[i,:]
        while True:
            B = A + randomVector(l)
            if B[0,0] >= 0 and B[0,1] >= 0: # is it within first quadrant?
                pairs.append(np.row_stack((A, B)))
                break
    return pairs


if __name__ == '__main__':
    
    draw = Turtle("Intersection")
    segments = randomSegments(15)

    for i, seg1 in enumerate(segments):
        for seg2 in segments[i+1:]:
            intersect = segmentIntersect(seg1, seg2)
            if intersect != None:
                draw.addPoint(intersect[0])

    for seg in segments:
        draw.addLineNumpy(seg[0], seg[1])

    draw.dumpImage()



