#######################################
#
#	Basic BMP library - bitmap, uses svg
#
#######################################

class bmp(object):
	def __init__(self, filename, x_table=1000, y_table=1000, side=10):
		self.x = x_table/2
		self.y = y_table/2
		self.filename = filename
		self.x_table = x_table
		self.y_table = y_table
		self.side = side
		self.my_file = open(self.filename + ".svg", "w")
		return

	def open(self):
		self.my_file.write('<svg width="'+str(self.x_table)+'" height="'+str(self.y_table)+'"> \n')

	def bit(self, x, y, rgb=[0,0,0]):	# rgb string such as (r, b, b), 0 <= r,g,b <= 255
		color = "("+str(rgb[0])+","+str(rgb[1])+","+str(rgb[2])+")"
		nx = str(self.side*x+self.x)
		ny = str(self.side*y+self.y)
		side = str(self.side)
		self.my_file.write('\t<rect x="'+nx+'" y="'+ny+'"\n\t\t  width="'+side+'"\n\t\t  height="'+side+'"\n\t\t  style="fill:rgb'+color+'; stroke-width:1; stroke:rgb'+color+'"/>\n')
		
	def offset(self, x, y):
		self.x = x
		self.y = y

	
	#def background(self):
	#	self.my_file.seek(0,2)
	#	self.my_file.write('<style type="text/css">')
	#	self.my_file.write('.background{background-color:red;}')
	#	self.my_file.write('</style>')

	def save(self):
		self.my_file.write('</svg>\n')
		self.my_file.close()

#######################################


picture = bmp("test", side=200)
picture.open()

picture.bit(0,0, [30,100,200])
#picture.bit(-0.5,1, [30,200,100])
#picture.bit(0.5,1, [30,200,100])
##for x in xrange(1,100):
##	for y in xrange(1,100):
##		picture.bit(x,y, [x+y, x, y])
#	
#
picture.save()
