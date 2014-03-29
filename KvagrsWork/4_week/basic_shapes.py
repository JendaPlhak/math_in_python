from PIL import Image
from math import tan, sqrt, pi, cos, sin, floor, ceil

""" Example of Image.new and putpixel - puts black pixel at [100,100] """
#im = Image.new("RGB", (2300, 200), "white")
#im.putpixel((100,100), (0,0,0))
#im.show()

WHITE = (255,255,255)
BLACK = (0,0,0)

def circle(r, x0=100, y0=100, fill=False, eps = 0.05):		# r = radius, the center of the circle = [x0,y0]
	coordinates = []
	for x in xrange(-r,r):
		for y in xrange(-r,r):
			if fill and x**2 + y**2 <= r**2:				# fill == True, therefore fill it!
				coordinates.append([x+x0,y+y0])				# creating the circle somwhere, and then moving it 
			if ~fill and abs((x**2 + y**2 - r**2)/float(r**2)) <= eps:	# fill == False 
				coordinates.append([x+x0,y+y0])
	return coordinates

def circle_par(r, start, end, thickness=20, fill=True):		# r = radius, start/end, absolute angles
	coordinates = []
	for t in xrange(start, end):
		r_t = (t*pi)/180									# Convert degrees to radians
		x = r+int(r*cos(r_t))								# Calculate coordinates		
		y = r+int(r*sin(r_t))
		coordinates.extend(circle(thickness, x+r, y+r, fill))
	return coordinates


def ellipse_par(a, b, start=0, end=360, thickness=5, fill=True):	# a, b axis, start/end, absolute angles
	coordinates = []
	for t in xrange(start, end):
		r_t = (t*pi)/180									# Convert degrees to radians
		x = a+int(a*cos(r_t))								# Calculate coordinates		
		y = b+int(b*sin(r_t))
		coordinates.extend(circle(thickness, x+a, y+b, fill))
	return coordinates

def spiral_par(start=0, end=3*360, thickness=3, fill=True):	# start/end, absolute angles
	# Calculate the offset
	#r_t = ((end%360)*pi)/180
	#a = int(end*cos(r_t) )
	#b = int(end*sin(r_t))
	coordinates = []
	for t in xrange(start, end):
		r_t = (t*pi)/180									# Convert degrees to radians
		x = 500+int(t*cos(r_t))								# Calculate coordinates		
		y = 500+int(t*sin(r_t))
		
		coordinates.extend(circle(thickness, x, y, fill))
	return coordinates

def equilateral_triangle(side):
	coordinates = []
	#print -side/2, side/2,int((sqrt(3)*side)/2)
	for x in xrange(-side/2, side/2):
		for y in xrange(int((sqrt(3)*side)/2)):
			v = (sqrt(3)*side)/2
			if y <= sqrt(3)*x+v and y <= -sqrt(3)*x+v:
				coordinates.append([x+side,-y+side])		# minus y-coordinate - [0,0] is top left and pos. directions are v and >
	return coordinates

#######################################

def standard_distence(A, B):
	return sqrt((A[0]-B[0])**2+(A[1]-B[1])**2)

def vectorize(A,B):
	return [B[0]-A[0],B[1]-A[1]]

def determinant(u, v):
	return u[0]*v[1]-v[0]*u[1]

def score_():
	pass

def iregular_polygon(vertices):
	maxDistance = standard_distence(vertices[0],vertices[1])
	tmp_list = list(vertices)
	for A in tmp_list:
		tmp_list.remove(A)
		for B in tmp_list:
			maxDistance = max(maxDistance, standard_distence(A,B))

	vertices.append(vertices[0])
	vectors = []
	for i in xrange(len(vertices)-1):
		vectors.append(vectorize(vertices[i],vertices[i+1]))
	vectors.append(vectors[0])

	score = 0
	for i in xrange(len(vectors)-1):

		print determinant(vectors[i],vectors[i+1])
		if determinant(vectors[i],vectors[i+1])>0:
			score += 1
		if determinant(vectors[i],vectors[i+1])<0:
			score -= 1

	return maxDistance, score

#######################################


def show(coordinates, width=1000, length=1000):
	im = Image.new("RGB", (width,length), "white")
	for pixel in coordinates:
		r = (pixel[0])%255
		g = (13*pixel[0])%255
		b = int(7*((pixel[0]+pixel[1])))%255
		#b = (200)

		color = (r,g,b)
		im.putpixel((pixel[0],pixel[1]), color)
	im.show()

if __name__ == '__main__':
	#show(circle(100, 300,300, fill=True))
	#show(spiral_par())
	#show(equilateral_triangle(100))
	show(circle_par(100, 0, 360, thickness=5, fill=True))