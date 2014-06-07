#! usr/bin/env python

from PIL  	   import Image
from math 	   import cos, sin, tan, pi
from itertools import product

def chessboard(frame=500, side=25, filename=''):

	im = Image.new("RGB", (frame, frame), (255,255,255))
	n = frame / 2
	for x, y in product(xrange(-n, n), xrange(-n, n)):
		mod_x = x % (side * 2)
		mod_y = y % (side * 2)

		if x**2 + y**2 - 10**4 < 0:
			if (mod_x < side) != (mod_y < side):
				col = (0,0,0)
			else:
				col = (255,255,255)
		else:
			if (mod_x < side) != (mod_y < side):
				col = (255,255,255)
			else:
				col = (0,0,0)


		im.putpixel((x + n, y + n), col)

	if filename:
		im.save('img/'+ filename +'.png')
	else:
		im.show()

	return
	
	

def circles(side=500, filename=''):
	
	im = Image.new("RGB", (side, side), (255,255,255))
	n = side / 2
	for x, y in product(xrange(-n, n), xrange(-n, n)):	
		#RBG_tuple = tuple( map( lambda x: int(x), [255 * sin(x**2), 255 * cos(y**2), 0 ] ) ) # irish
		#RBG_tuple = tuple( map( lambda x: int(x), [255 * sin(pi * x * 0.09), 255 * cos(pi * y * 0.09), 255 * sin(pi * x * y * 0.09)] ) ) # color circle
		#RBG_tuple = tuple( map( lambda x: int(x), [255 * sin(pi * x * 0.09), 255 * cos(pi * y * 0.09), 100 *(pi * y * 0.09)] ) ) #water
		#RBG_tuple = tuple( map( lambda x: int(x), 3 * [255 * (cos(x / 5)**2 + sin(y / 5)**2)**0.5]) ) # modern squares
		#RBG_tuple = tuple( map( lambda x: int(x), [x+y,x-y,x*y]) )
		
		if max(abs(x), abs(y)) < 100:
			RBG_tuple = tuple( map( lambda x: int(x), 3 * [ 127 * (sin((x**2 +  y**2)**0.5 / pi / 2) + 1)]) )
		else:
			RBG_tuple = tuple( map( lambda x: int(x), 3 * [ 255 - 127 * (sin((x**2 +  y**2)**0.5 / pi / 2) + 1)]) )

		im.putpixel( (x + n, y + n), RBG_tuple )

	if filename:
		im.save('img/'+ filename +'.png')
	else:
		im.show()


def lines(side=500, filename=''):

	im = Image.new("RGB", (side, side), (255,255,255))
	n = side / 2
	for x, y in product(xrange(-n, n), xrange(-n, n)):	
		RBG_tuple = tuple( map( lambda x: 127 * int(x), [max(x, 0), max(y,0), max(x, y)]) )
		im.putpixel( (x + n, y + n), RBG_tuple )

	if filename:
		im.save('img/'+ filename +'.png')
	else:
		im.show()

if __name__ == '__main__':

	#circles(filename='circle')
	#chessboard(filename='chessboard')
	lines(filename='lines')