from PIL  import Image
from math import cos, sin, sqrt

def second_effect(side=500):
	
	im = Image.new("RGB", (side, side), (255,255,255))
	for x in range( -side / 2, side / 2):
		for y in range( -side / 2, side / 2  ):
			
			"""
			the magic goes here...
			"""

			im.putpixel( (x + side / 2, y + side / 2), (red, green, blue) )
	im.show()

if __name__ == '__main__':

	second_effect()