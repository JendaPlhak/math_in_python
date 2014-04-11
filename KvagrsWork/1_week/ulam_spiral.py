#!/usr/bin/env python
import sys
for i in xrange(8):
	sys.path.append('../' + str(i) + '_week')

from convex_wrapping import norm, angle
from turtle_lib import Turtle
from math import sqrt, ceil
import itertools

def sieveOfEratosthenes(n):

	numbers = [True] * n
	i 		= 2
	while i**2 < n:
		for j in range(2, int(n / i) + 1):
			numbers[ ( i * j ) - 1 ] = False
		i += 1

	primes = []
	for j in range(1, n):
		if numbers[j] == True:
			primes.append(j + 1)

	return primes


def cmp2DIntegers(u, v):

	if norm(u) <= norm(v) and angle( u, [1,0] ) < angle( v, [1,0] ):
		return -1
	elif norm(v) <= norm(u) and angle( v, [1,0] ) < angle( u, [1,0] ):
		return 1
	else:
		return 0


def order2DIntegers(n):

	points = []
	index  = int(ceil( ( n**(0.5) ) / 2))		# basic guess, won't need so much 2-tuples

	for x, y in itertools.product( xrange( -index, index ), xrange( -index, index )):
		points.append( [x + 1, y + 1] )			# +1 offset, depends on the direction of spiral
		
	points.remove( [0,0] )
	points = sorted( points, cmp=cmp2DIntegers )
	return [0, 0] + points[:n]


if __name__ == '__main__':

	ulam = Turtle()
	ulam.forward(50)
	ulam.draw_object(filename='ulam_spiral')