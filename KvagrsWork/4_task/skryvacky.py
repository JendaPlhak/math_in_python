from PIL import Image



""" Task 1 """
im = Image.open("img/skryvacka1.png")
pix = im.load()
for x in xrange(im.size[0]):
	for y in xrange(im.size[1]):
		
		pix[x,y] = (0,0,pix[x,y][2]*255)
		
im.show()
im.save("solved1.png")


""" Task 3 
im = Image.open("img/skryvacka3.png")
pix = im.load()


for x in xrange(0,im.size[0]-2,2):
	for y in xrange(im.size[1]):
		if bool(pix[x,y][0]) != bool(pix[x+2,y][0]):
			pix[x,y] = (0,0,0)
		else:
			pix[x,y] = (255,255,255)
for x in xrange(im.size[0]):
	for y in xrange(0,im.size[1]-2,2):
		if bool(pix[x,y][0]) != bool(pix[x,y+2][0]):
			pix[x,y] = (0,0,0)
		else:
			pix[x,y] = (255,255,255)

im.show()
im.save("solved3.png")
"""


"""
r = []
g = []
b = []
im = Image.open("img/skryvacka2.png")
pix = im.load()
for x in xrange(im.size[0]):
	for y in xrange(im.size[1]):
		if pix[x,y][0] not in r:
			r.append(pix[x,y][0])
		if pix[x,y][1] not in g:
			g.append(pix[x,y][1])
		if pix[x,y][2] not in b:
			b.append(pix[x,y][2])
		if pix[x,y][0] > 200 and pix[x,y][1] < 100 and pix[x,y][2] > 200:
			pix[x,y] = (0,0,0)
		if pix[x,y][0] < 100 and pix[x,y][1] < 100 and pix[x,y][2] > 200:
			pix[x,y] = (0,0,0)
		if pix[x,y][0] < 100 and pix[x,y][1] > 100 and pix[x,y][2] < 100:
			pix[x,y] = (0,0,0)

miss_r = []
miss_g = []
miss_b = []
for i in range(256):
	if i not in r:
		miss_r.append(i)
	if i not in g:
		miss_g.append(i)
	if i not in b:
		miss_b.append(i)



#print sorted(miss_r)
#print sorted(miss_g)
#print sorted(miss_b)
#print
#a = [num for num in range(255) if num not in miss_g]
#print a
im.show()
"""