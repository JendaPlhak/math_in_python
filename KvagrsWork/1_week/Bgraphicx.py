#######################################
#
#	Task 1 part B, vector and bitmap graphics
#
#######################################

from svglib import svg
from bmplib import bmp

def fixed_length_segment(pic, side, n):	# side = length of segment, n = number of steps
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

#######################################

def color_flow(side):
	bits = []
	for i in range(side):
		for j in range(side):
			bits.append([i,j,[100+i, j, i+j]])
	return bits



draw = bmp("test", 1000, 1000, 2)
draw.open()
draw.offset(500,500)

side = 100
bits = color_flow(side)

for i in range(side**2):
	draw.bit(bits[i][0], bits[i][1], bits[i][2])

#n = 10
#lines = fixed_length_segment(draw, 200, n)
#for i in range(4*(n+1)):
#	draw.line(lines[i][0], lines[i][1], lines[i][2], lines[i][3], width="2")



draw.save()