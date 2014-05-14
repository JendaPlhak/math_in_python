#!/usr/bin/env python

import sys
sys.path.append("../3_task")
from PIL           import Image
from random        import randint, random
from bisect        import bisect_right
from test_pictures import regularPolygon
from Turtle        import Turtle



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



def randomPolygon(n=3, r=1/2., n_iter=100000, a=300, size=1000, path="img/randomSierpinski.png"):
    
    vertices = regularPolygon(Turtle("randomPolygon", (250,250)), a, n)
    img      = Image.new('RGB', (size,size), 'white')
    
    point = 10
    for k, i in enumerate(WeightedRandom(n_iter, [1] * n)):
        vect  = vertices[i] - point
        point = point + (1-r)*vect
        if k > 1000:
            img.putpixel( (int(point.real), int(point.imag)), (255 - int(255 * float(k) / n_iter),
                                                               0,
                                                               int(255 * float(k) / n_iter)) )

    img.save(path)



if __name__ == '__main__':

    randomPolygon()
