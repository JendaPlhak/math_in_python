#! usr/bin/env python

import itertools

from PIL  import Image
from math import cos, sin, pi

def chessboard_effect(sied=500):

	pass
	

def circle_effect(side=500):
	
	im = Image.new("RGB", (side, side), (255,255,255))
	n = side / 2
	for x, y in itertools.product(xrange(-n, n), xrange(-n, n)):	
		#RBG_tuple = tuple( map( lambda x: int(x), [255 * sin(x**2), 255 * cos(y**2), 0 ] ) ) # irish
		#RBG_tuple = tuple( map( lambda x: int(x), [255 * sin(pi * x * 0.09), 255 * cos(pi * y * 0.09), 255 * sin(pi * x * y * 0.09)] ) ) # color circle
		#RBG_tuple = tuple( map( lambda x: int(x), [255 * sin(pi * x * 0.09), 255 * cos(pi * y * 0.09), 100 *(pi * y * 0.09)] ) ) #water
		#RBG_tuple = tuple( map( lambda x: int(x), 3 * [255 * (cos(x / 5)**2 + sin(y / 5)**2)**0.5]) ) # modern squares
		#RBG_tuple = tuple( map( lambda x: int(x), [x+y,x-y,x*y]) )
#		if x**2 + y**2 - 100**2 < 0.001:
		RBG_tuple = tuple( map( lambda x: int(x), 3 * [127 * (cos(x/pi) + 1)]) )
#		else:
#			RBG_tuple = tuple( map( lambda x: int(x), 3 * [255 - (127 * (cos(x / pi**2) + sin(y / pi**2)))]) )
		#print ' '.join(str(RBG_tuple))

		im.putpixel( (x + n, y + n), RBG_tuple )
	im.putpixel((n,n), (255,0,0))
	im.show()


def rgb_lines(side=500):

	im = Image.new("RGB", (side, side), (255,255,255))
	n = side / 2
	for x, y in itertools.product(xrange(-n, n), xrange(-n, n)):	
		RBG_tuple = tuple( map( lambda x: 127 * int(x), [x, 0, 0]) )
		im.putpixel( (x + n, y + n), RBG_tuple )
	im.putpixel((n,n), (255,0,0))
	im.show()

if __name__ == '__main__':

	#circle_effect()
	rgb_lines()