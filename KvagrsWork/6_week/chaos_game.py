from PIL  	import Image
from math 	import cos, sin, pi
from random import randint


def chaos_game(n, r, side=100, iteration=100):		# n = the number of points, r 
	
	base = []
	angle  = pi/2
	for i in xrange(n):									# draw regular n-polygon
		x = int(side*cos(angle))
		y = int(side*sin(angle))
		angle += 2*pi/n
		base.append([x+side,-y+side])

	x = randint(0, side-1)
	y = randint(0, side-1)

	pixels = [[x,y]]
	for i in xrange(iteration):
		V = base[randint(0,n-1)]
		x = (x+V[0])*r
		y = (y+V[1])*r
		pixels.append([x,y])

	pixels.extend(base)
	#for pixel in pixels:
	#	pixel[0] += side
	#	pixel[1] += side

	return pixels


def draw_chaos_game(n, r, save=False, filename=None, side=100):

	im = Image.new("RGB", (1000, 1000), (255,255,255))
	pixels = chaos_game(n,r,side)

	for pixel in pixels:
		im.putpixel(pixel, (255,0,0))

	im.show()

	if save:
		im.save()


if __name__ == '__main__':
	
	draw_chaos_game(3,1/2,side=100)