from PIL  	import Image
from math 	import cos, sin, pi,sqrt
from random import randint
import random


def weighted_random_point(points, weights):											# Different possibilities of chosing some point, weights == [W1,W2,W3]
	
	weighted_points = []
	for i, point in enumerate(points):
		weighted_points.append( point * weights[i] )

	return random.choice( weighted_points )


def chaos_game(n, r, weights, side=100, iteration=1000, regular=True):		# n = the number of points, r 
	
	edge_points = []
	if regular:
		angle  = pi/2
		for i in xrange(n):											# draw vertices of regular n-polygon
			x = int(side*cos(angle))
			y = int(side*sin(angle))
			angle += 2*pi/n
			edge_points.append( [x + side,-y + side] )
	
	else:
		for i in xrange(n):
			x = randint(0,side)
			y = randint(0,side)
			edge_points.append( [x + side, y + side] )


	x      = randint(0, side-1)
	y 	   = randint(0, side-1)
	pixels = [[x,y]]

	for i in xrange(iteration):
		rand = weighted_random_point( edge_points, weights )
		x 	 = int(( x + rand[0]) * r)
		y 	 = int(( y + rand[1]) * r)
		if i > 100:
			pixels.append( [x + side, y + side] )

	pixels.extend( edge_points )
	return pixels


def draw_chaos_game(n, r, weights, side=100, iteration=100,  regular=True, save=False, filename=None):

	pixels = chaos_game(n, r, weights, side, iteration, regular)
	im 	   = Image.new("RGB", (1000, 1000), (255,255,255))

	for pixel in pixels:
		im.putpixel(pixel, (0,0,0))

	im.show()

	if save:
		im.save('filename')


if __name__ == '__main__':
	
	draw_chaos_game(n=3, r=0.5, weights=[1,1,1], side=200, iteration=100000, regular=True)