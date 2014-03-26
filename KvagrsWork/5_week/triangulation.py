import svgwrite
import os
from random 				import random, randint
from math 					import sqrt, cos, sin
from segment_intersection 	import cross_point, generate_data, dist


def join_points(points):								# creates a segment for each pair of points

	segments = []
	tmp_list = points[:]

	for A in points:
		tmp_list.remove(A)
		for B in tmp_list:
				segments.append(A+B)
	return segments


def sort_segments(segments):

	for i in xrange(len(segments)):
		for j in xrange(i,len(segments)):
			if dist(segments[i][2:],segments[i][:2]) >= dist(segments[j][2:],segments[j][:2]):
				tmp  = segments[j]
				segments[j] = segments[i]
				segments[i] = tmp
	return


def triangulation(n, length=100, min_side=False):

	points 		= generate_data(n, length, segments=False)
	segments 	= join_points(points)

	if min_side:							# If True sorts segments by the length of the side of triangles
		sort_segments(segments)

	fin_segments= [segments[0]]
	crosses 	= []

	segments.pop(0)
	for seg1 in segments:
		add = True
		for seg2 in fin_segments:
			if cross_point(seg1, seg2)[1] == True:
				add = False
				break
		if add:
			fin_segments.append(seg1)
	
	return points, fin_segments

def draw_triangulation(n):

	im = svgwrite.drawing.Drawing()
	points, segments = triangulation(n, length=120, min_side=True)

	for seg in segments:
		im.add( im.line(	start 	= (seg[0], seg[1]),\
							end 	= (seg[2], seg[3]),\
							stroke 	= 'black'))
	for point in points:
		im.add( im.circle( 	center	= (point[0],point[1]),\
							r 		= 2,\
							stroke 	= 'black'))

	if os.path.isdir("../../webserver/layout2/static/img/KvagrsWork/5_week/"):

		im.saveas("../../webserver/layout2/static/img/KvagrsWork/5_week/triangulation.svg")
		return "../../webserver/layout2/static/img/KvagrsWork/5_week/triangulation.svg"
	else:

		im.saveas("/home/ubuntu/math_in_python/webserver/layout2/static/img/KvagrsWork/5_week/triangulation.svg")
		return "/home/ubuntu/math_in_python/webserver/layout2/static/img/KvagrsWork/5_week/triangulation.svg"
	


if __name__ == '__main__':

	print "Drawing triangulation for 10 points"
	draw_triangulation(10)