#!/usr/bin/env python
import sys

sys.path.append("../4_task")

import svgwrite
from random 				import random, randint
from math 					import sqrt, cos, sin, atan, acos, pi
from segment_intersection 	import cross_point, generate_data, dist
from polygon 				import determinant

def find_right(points):						# find the rightest point in the plane

	right = points[0]

	for point in points:
		if right[0] <= point[0]:
			right = point
	return right


def norm(u):

	return (dot_product(u,u))**0.5


def dot_product(u,v):

	S = 0
	for i in xrange(len(u)):
		S += u[i]*v[i]

	#if S == 0:
		#print u, v
	return S


def angle(u,v):

	arg = ( dot_product(u,v) / (norm(u) * norm(v)) )

	return acos(arg)



def degToRad(phi):		# Conversion function from degrees to radians
		r_phi = (phi*pi)/180
		return r_phi


def vectorize(A,B):

	u0 = B[0]-A[0]
	u1 = B[1]-A[1]

	return [u0, u1]


def line_print(data):

	for item in data:
		print data


def convex_wrapping(n):


	points 	      = generate_data(n)			# generate points in plane
	backup_points = points 						# backup for return
	
	r_point	= find_right(points)				# find the rightest point
	#fixed_v	= vectorize([0,1], r_point)			# starting vector to which will be calculated the angle

	points.remove(r_point)						# remove the r_point from points, but put it back later so it can cycle
	next = points[0]							# get the first point, why not. No need for random

	edges 	= []
	fixed_v	= vectorize([0,1], r_point)
	free_v  = vectorize(next, r_point)
	angle   = angle(fixed_v, free_v)

	while next != r_point:
		for point in points:
			free_v  = vectorize(point, r_point)
			n_angle = angle(fixed_v, free_v)
			if angle > n_angle:
				next  = point
				angle = n_angle

		edges.append(r_point + next)
		points.append(r_point)
		r_point = next
		points.remove()


	return fix_points, edges




if __name__ == '__main__':

	"""	
	points, edges = convex_wrapping(10)
	im 	 = svgwrite.drawing.Drawing()

	print edges

	for point in points:
		im.add( im.circle(	center 	= (point[0],point[1]),\
							r 		= 2,\
							stroke	= 'black'))
	
	print
	line_print(edges)
	for line in edges:
		im.add( im.line(start 	= (line[0],line[1]),\
						end 	= (line[2],line[3]),\
						stroke	= 'black'))
	im.saveas("convex_wrapping.svg")
	"""

	#num = dot_product([0,1], [-1,1])
	#den = norm([0,1]) * norm([-1,1])
	#print acos(num / den)
#
#	#num = dot_product([0,1], [-1,2])
#	#den = norm([0,1]) * norm([-1,2])
	#print acos(num / den)