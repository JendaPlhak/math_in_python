#!/usr/bin/env python
import sys
sys.path.append("../3_task")
import numpy as np
from Turtle import Turtle
from math   import pi



class Polygon():

    def __init__(self, vertices):

        self.n     = len(vertices)
        self.vert  = [ np.array(vortex) for vortex in vertices] 
        self.edges = [ self.vert[(i+1)%self.n] - self.vert[i] for i in xrange(self.n)]

    # Calculation using Ray casting method. Ray in direction of S-P.
    def testIn(self, P):

        S = np.array((-1*pi,-1))
        P = np.array(P)
        n_intersections = 0

        for vertex in self.vert:
            if (vertex == P).all():
                return True
            
        PS = S-P
        for i in xrange(self.n):
            A = self.vert[i]
            B = self.vert[(i + 1) % self.n]

            PA = A-P
            PB = B-P

            det_PS_PA = np.linalg.det(np.column_stack((PS,PA)))
            det_PS_PB = np.linalg.det(np.column_stack((PS,PB)))
            det_PB_PA = np.linalg.det(np.column_stack((PB,PA)))

            # Compare vectors orientation 
            if 0 >= det_PS_PA * det_PS_PB and \
               0 <  det_PS_PA * det_PB_PA:
                n_intersections += 1
        return bool(n_intersections % 2)
        

    def drawPolygon(self):

        self.draw = Turtle("Polygon")

        for i in xrange(self.n):
            self.draw.addLineNumpy(self.vert[i], self.vert[(i+1) % self.n])


if __name__ == '__main__':
    
    p = Polygon([(10, 10), (180, 20), (160, 150), (100, 50), (10, 180)])
    p.drawPolygon()
    P = (150, 100)
    p.draw.addPoint(P)
    
    if p.testIn(P):
        p.draw.text("It's IN!",  fill="blue")
    else:
        p.draw.text("It's OUT!", fill="blue")
    p.draw.dumpImage()


        

