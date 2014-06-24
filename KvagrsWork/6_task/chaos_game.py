#!/usr/bin/env python
import sys
import os
sys.path.append("../4_task")

from PIL       import Image
from math      import cos, sin, pi,sqrt
from random    import randint
from itertools import product
import random

from basic_shapes import movePointsTowardsOrigin

class ChaosGame():

    def __init__(self, n, r=0.5, side=200, regular=True):

        self.n        = n
        self.r        = r
        self.pixels   = []
        self.vertices = []
        self.weights  = [[i * (1. / n), (i + 1) * (1. / n)] for i in xrange(n)]
        self.side     = side

        if regular:
            angle  = pi / 2
            # draw vertices of regular n-polygon
            for i in xrange(n):
                x = int(side * cos(angle))
                y = int(side * sin(angle))
                angle += (2 * pi / n)
                self.vertices.append( [x + side,-y + side] )


        self.pixels.extend( self.vertices )

        return


    def add_points(self, iteration=100000):

        x, y = randint(0, self.side), randint(0, self.side)

        for i in xrange(iteration):
            fixed = self.random_vertex()

            x    = int(( x + fixed[0]) * self.r)
            y    = int(( y + fixed[1]) * self.r)
            if i > 1000:
                self.pixels.append( [x + self.side, y + self.side] )
            

        return


    def random_vertex(self):
    # returns random vertex based on the weights

        value =  random.uniform(0,1)
        for i, weight in enumerate( self.weights ):
            if weight[0] <= value and value <= weight[1]:
                index = i
                break

        return self.vertices[i]


    def draw(self, filename=''):

        self.pixels, size = movePointsTowardsOrigin( self.pixels )
        im = Image.new("RGB", tuple(size), (255,255,255))

        for pixel in self.pixels:
            im.putpixel(pixel, (0,0,0))

        if filename:
            im.save('img/'+ filename +'.png')
        else:
            im.show()


def weighted_random_point(points, weights):
# Different possibilities of chosing some point, weights == [W1,W2,W3]
    
    weighted_points = []
    for i, point in enumerate(points):
        weighted_points.append( point * weights[i] )

    return random.choice( weighted_points )


def chaos_game(n, r, weights, side=100, iteration=1000, regular=True):
# n = the number of points, r 
    
    edge_points = []
    if regular:
        angle  = pi / 2
        # draw vertices of regular n-polygon
        for i in xrange(n):
            x = int(side*cos(angle))
            y = int(side*sin(angle))
            angle += (2 * pi / n)
            edge_points.append( [x + side,-y + side] )
    
    else:
        for i in xrange(n):
            x = randint(0,side)
            y = randint(0,side)
            edge_points.append( [x + side, y + side] )


    x      = randint(0, side - 1)
    y      = randint(0, side - 1)
    pixels = [[x,y]]

    for i in xrange(iteration):
        rand = weighted_random_point( edge_points, weights )
        x    = int(( x + rand[0]) * r)
        y    = int(( y + rand[1]) * r)
        if i > 100:
            pixels.append( [x + side, y + side] )

    return pixels


def draw_chaos_game(pixels, filename=''):

    #if weights == None:
    #    weights = [1] * n

    #pixels = chaos_game(n, r, weights, side, iteration, regular)
    pixels, size = movePointsTowardsOrigin( pixels )
    print size
    #print pixels
    im = Image.new("RGB", tuple(size), (255,255,255))

    for pixel in pixels:
        im.putpixel(pixel, (0,0,0))

    if filename:
        im.save('img/'+ filename +'.png')
    else:
        im.show()


if __name__ == '__main__':
        
    #pixels = chaos_game(n=3, r=0.5, weights=[1,1,1], side=200, iteration=1000000, regular=True)
    #print len(pixels)
    #draw_chaos_game(pixels, filename='sierpinski_gasket')
    #pixels = chaos_game(n=5, r=0.2, weights=[1,1,1,1,1], side=200, iteration=100000, regular=True)
    #draw_chaos_game(pixels, filename='sierpinski_gasket')
    for n, r in product([3,5,7,11],[0.1,0.255,0.5,0.94]):
        chaos_game = ChaosGame(n=n, r=r)
        chaos_game.add_points()
        chaos_game.draw('chaos_game_'+str(n)+'_'+str(r))