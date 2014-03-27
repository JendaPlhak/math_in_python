import svgwrite
from random 				import random, randint
from math 					import sqrt, cos, sin, atan, acos
from segment_intersection 	import cross_point, generate_data, dist

def find_right(points):						# find the rightest point in the plane

	right = points[0]

	for point in points:
		if right[0] <= point[0]:
			right = point
	return right


def norm(u):

	return sqrt(dot_product(u,u))


def dot_product(u,v):

	S = 0
	for i in xrange(len(u)):
		S += u[i]*v[i]

	if S == 0:
		print u, v
	return S


def angle(u,v):

	arg = ( dot_product(u,v) / (norm(u)*norm(v)) )

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

	points 	= generate_data(n)
	fix_points = points
	line_print(points)
	right 	= find_right(points)
	edges	= []
	fixed_v	= [0,1]

	points.remove(right)
	next = points[0]
	#points.remove(next)
	#while next == right:
	#	i 	 = randint(1, len(points)-1)
	#	next = points[i]
	
	var_v 	  = vectorize(right, next)
	min_angle =  angle(fixed_v, var_v)
	print "Min angel"
	print min_angle

	while next != right:
		for i, point in enumerate(points):

			if min_angle > angle(fixed_v, vectorize(right, point)):
				next 	  = point
				var_v 	  = vectorize(right, next)
				min_angle = angle(fixed_v, vectorize(right, point))
				print "Min angel"
				print min_angle

		edges.append( right+next )
		points.append(right)
		right = next
		points.remove(next)
		

	return fix_points, edges




if __name__ == '__main__':

	
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
	