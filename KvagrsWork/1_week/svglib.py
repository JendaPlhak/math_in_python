#######################################
#
#	Basic SVG library - line, circle, bitmap
#
#######################################

class svg(object):
	def __init__(self, filename, x_table, y_table):
		self.x = x_table/2
		self.y = y_table/2
		self.filename = filename
		self.x_table = x_table
		self.y_table = y_table
		self.my_file = open(self.filename + ".svg", "w")
		return

	def open(self):
		self.my_file.write('<svg width="'+str(self.x_table)+'" height="'+str(self.y_table)+'"> \n')

	def line(self, x1, y1, x2, y2, width="2", color="black"):
		n_x1 = str(self.x + x1)
		n_x2 = str(self.x + x2)
		n_y1 = str(self.x + y1)
		n_y2 = str(self.x + y2)
		self.my_file.write('<line x1="'+n_x1+'" y1="'+n_y1+'"\n\t  x2="'+n_x2+'" y2="'+n_y2+'"\n\t  stroke-width="'+width+'"\n\t  stroke="'+color+'"/>\n')
	
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

#picture = svg("test", 100,100)
#picture.open()
#picture.line(2,2,8,9)
#picture.save()