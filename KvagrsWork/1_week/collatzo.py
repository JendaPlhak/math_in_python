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


points=[]
for i in range(1,8000):
	points.append([i, collSteps(i)])
	plt.plot( [i],[collSteps(i)[1]], 'ko' )				# collSteps(i)[0] are steps, collSteps(i)[1] are max num in collatzo series

plt.axis([0,5000,0,5000])
plt.savefig('collatzo_max.png')