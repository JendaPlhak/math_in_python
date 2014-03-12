#######################################
#
# Pascals triangle, modulo
#
#######################################

from bmplib import bmp

def pascals_triangle(n):	# n = number of layers in the triangle
	layers = []
	layers.append([1])
	layers.append([1,1])

	for i in range(2,n):
		tmp_list=[]
		tmp_list.append(1)
		for j in range(i-1):
			tmp_list.append(layers[i-1][j] + layers[i-1][j+1] )
		else:
			tmp_list.append(1)
		layers.append(tmp_list)
	return layers

n = 20
mod = 13
side = 10


layers = pascals_triangle(n)

triangle = bmp("triangle", x_table=2000, x_offset=1000, y_table=2000, y_offset=0, side=side)
triangle.open()

colors = []
for x in range(1,mod+1):
	colors.append([(100+255/(x/5.))%255,(150+255/(x/5.))%255,(30+255/(x/5.))%255])

for y in range(n):
	for x in range(len(layers[y])):
		nx = (x + n/2 - (y+0.5)/2)		# off set
		color = colors[layers[y][x]%mod]
		triangle.bit(nx, y, color)

	

triangle.save()