#######################################
#
# Plot collatzo steps for natural N
#
#######################################

import matplotlib.pyplot as plt

def collSteps(n):
	steps = 0
	maxN = n
	while n!=1:
		#print n
		if n%2 == 0:
			n /= 2
		else:
			n = 3*n + 1
		steps += 1
		maxN = max(maxN, n)
	return steps, maxN

#######################################

#print collSteps(8000) 
#plt.plot([15],[collSteps(15)[1]],'ko')

points=[]
for i in range(1,8000):
	points.append([i, collSteps(i)])
	plt.plot( [i],[collSteps(i)[0]], 'ko' )

#print points

plt.axis([0,8000,0,300])
plt.savefig('collatzo.png')