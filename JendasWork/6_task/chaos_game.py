#!/usr/bin/env python

import sys
sys.path.append("../3_task")
from PIL      import Image
from random   import randint, random
from bisect   import bisect_right
from test_fun import regularPolygon
from Turtle   import Turtle



class WeightedRandom():

    def __init__(self, n, weights):
        
        self.totals   = []
        running_total = 0

        self.n = n
        self.i = 0

        for w in weights:
            running_total += w
            self.totals.append(running_total)


    def next(self):

        if self.i < self.n:
            self.i += 1
            rnd     = random() * self.totals[-1]
            return bisect_right(self.totals, rnd)

        else:
            raise StopIteration


    def __iter__(self):
        return self



def randomPolygon(n=3, r=1/2., n_iter=100000, a=400, size=1000, path="img/randomPolygon.png"):
    
    vertices = regularPolygon(Turtle("randomPolygon", (250,250)), a, n)
    img      = Image.new('RGB', (size,size), 'white')
    
    point = 0
    for i in WeightedRandom(n_iter, (1,1,2)):
        vect  = vertices[i] - point
        point = point + r*vect
        img.putpixel( (int(point.real), int(point.imag)), (0,0,0) )

    img.save(path)



if __name__ == '__main__':

    randomPolygon()
