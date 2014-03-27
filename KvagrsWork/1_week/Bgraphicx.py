#######################################
#
#	Task 1 part B, vector and bitmap graphics
#
#######################################

import svgwrite
from PIL import Image

def fixed_length_segment(side, n):	# side = length of segment, n = number of steps

	step = side/n
	lines = []
	for i in range(n+1):
		print i
		x0 = 0
		x1 = side - step*i
		y0 = step*i
		y1 = 0
		lines.append([x0, y0, x1, y1])
		lines.append([x0, -y0, -x1, y1])
		lines.append([x0, y0, -x1, y1])
		lines.append([x0, -y0, x1, y1])
	return lines


def draw_fixed_length_segment(side, n):

	im 	  = svgwrite.drawing.Drawing()
	lines = fixed_length_segment(side, n)

	for line in lines:
		A = (line[0]+side, line[1]+side)
		B = (line[2]+side, line[3]+side)
		im.add( im.line(	start = A,\
							end   = B,\
							stroke= 'black' ))
	im.saveas('orion.svg')


#######################################

def color_flow(side):

	bits = []
	for x in xrange(side):
		for y in xrange(side):
			bits.append( [(x,y),(100+x, y, x+y)])
	return bits

def draw_color_flow(side):

	pixels = color_flow(side)
	im 	   = Image.new("RGB",(side,side),(0,0,0))

	for pixel in pixels:
		im.putpixel(pixel[0], pixel[1])

	im.save('color_flow.bmp')

#######################################


if __name__ == '__main__':

	draw_fixed_length_segment(200,10)
	draw_color_flow(200)