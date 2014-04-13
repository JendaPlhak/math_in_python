#!/usr/bin/env python
import matplotlib
matplotlib.use('Agg')			# won't display plt
import matplotlib.pyplot as plt

def collSteps(n):
	steps 	= 0
	maxN 	= n
	while n != 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = 3 * n + 1
		steps += 1
		maxN = max(maxN, n)
	return steps, maxN


def plot_collatzo(x=8000, y=300, maxNumber=False):


	points=[]
	plt.axis([0,x,0,y])
	for i in range(1,x):
		points.append([i, collSteps(i)])

		plt.xlabel('Natural numbers')
		if maxNumber:	
			plt.plot( [i],[collSteps(i)[1]], 'ko' )		# collSteps(i)[1] for max
			plt.ylabel('Maximal number aj')
			plt.savefig('img/collatzo_max.png')
		else:
			plt.plot( [i],[collSteps(i)[0]], 'ko' )		# collSteps(i)[0] for steps
			plt.ylabel('Number of steps')
			plt.savefig('img/collatzo_steps.png')

	return


if __name__ == '__main__':

	plot_collatzo(x=8000, y=300)
	#plot_collatzo(x=5000, y=5000, maxNumber=True)
