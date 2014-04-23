import svgwrite
import os
from random import random, randint
from math 	import sqrt, cos, sin

def dist(A,B):

	return sqrt( (A[0]-B[0])**2 + (A[1]-B[1])**2 )			# euclidean distance/norm


def cross_point(u, v):										# u, v are lists, |u| = 4 = |v|

	# 	Using intersection of two lines
	#
	# 	s: y = k1*x + q1
	# 	t: y = k1*x + q1

	A,B,C,D = u[:2],u[2:],v[:2],v[2:]
	x0,y0 = A
	x1,y1 = B
	x2,y2 = C
	x3,y3 = D
	
	if x0 - x1 == 0 or x2 - x3 == 0:
		return (None, None), False

	k1 = (y0-y1)/(x0-x1)									# actual magic, k1,2 and q1,2 are coefficients for lines, 
	q1 = y0-k1*x0
	k2 = (y2-y3)/(x2-x3)
	q2 = y2-k2*x2

	if k1 == k2:
		return (None, None), False

	Px = (q2-q1)/(k1-k2)									# [Px,Py] is the cross point
	Py = k1*Px+q1

	P = [Px,Py]

	if 	abs(dist(A,B) - dist(A,P) - dist(P,B)) < 0.01 and \
		abs(dist(C,D) - dist(C,P) - dist(P,D)) < 0.01 and \
		A not in [C,D] and B not in [C,D]:
		return (Px,Py), True

	else:
		return (None, None), False


def generate_data(n, l=100, segments=False):

	data = []
	for i in xrange(n):
		x = random()*2*l+l  								# generate random x,y starting coordinates
		y = random()*2*l+l
		if segments:
			angle = randint(0,360) 							# generate random angle 
			nx = x+l*cos(angle) 							# calculate new coordinates
			ny = y+l*sin(angle)
			data.append([x,y,nx,ny])
		else:
			data.append([x,y])
	return data	


def segment_intersection(n, length=100):

	segments = generate_data(n, length, segments=True)
	tmp_list = list(segments)
	seg_intersect = []
	N = 0
	for segA in segments:									# iterate over all segments
		tmp_list.remove(segA)								# remove the one you have started from

		for segB in tmp_list:
			if cross_point(segA, segB)[1]:
				seg_intersect.append(cross_point(segA, segB)[0])
	return	segments, seg_intersect


def draw_segment_intersection(n, length=100):

	im = svgwrite.drawing.Drawing()
	segments, points = segment_intersection(n, length)

	for seg in segments:
		im.add( im.line(	start 	= (seg[0],seg[1]),\
							end 	= (seg[2],seg[3]),\
							stroke  = 'black'))
	for point in points:
		im.add( im.circle(	center 	= point,\
							r 		= 2,\
							stroke	= 'red'))

	if os.path.isdir("../../webserver/layout2/static/img/KvagrsWork/5_taswk/"):

		im.saveas("../../webserver/layout2/static/img/KvagrsWork/5_task/intersection.svg")
		return "../../webserver/layout2/static/img/KvagrsWork/5_task/intersection.svg"
	else:

		im.saveas("/home/ubuntu/math_in_python/webserver/layout2/static/img/KvagrsWork/5_taswk/intersection.svg")
		return "/home/ubuntu/math_in_python/webserver/layout2/static/img/KvagrsWork/5_taswk/intersection.svg"
	
if __name__ == '__main__':

	print "Draw segments and their cross points for"
	print "10 points and length 100 of each segment."
	#draw_segment_intersection(10,100)

	print cross_point([0,0,1,10],[5,5,-5,5])