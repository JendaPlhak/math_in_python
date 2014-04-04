#!/usr/bin/env python
import matplotlib.pyplot as plt

def collSteps(n):
	steps 	= 0
	maxN 	= n

	total = 1

	while n!=1:
		total += n
		#print n
		if n%2 == 0:
			n /= 2
		else:
			n = 3*n + 1
		steps += 1
		maxN = max(maxN, n)
	return steps, maxN, 1000/total


def plot_collatzo(x=8000, y=300, maxNumber=False, total=False):

	points=[]
	plt.axis([0,x,0,y])
	for i in range(1,x):
		points.append([i, collSteps(i)])

		if maxNumber:
			plt.plot( [i],[collSteps(i)[1]], 'ko' )      # collSteps(i)[0] are steps, collSteps(i)[1] are max num in collatzo series
			plt.ylabel('Maximal number aj')
			plt.savefig('collatzo_max.png')

		elif total:
			plt.plot( [i],[collSteps(i)[2]], 'ko' )
			plt.ylabel('Number of steps')
			plt.savefig('collatzo_inverse.png')

		else:
			plt.plot( [i],[collSteps(i)[0]], 'ko' )
			plt.ylabel('Number of steps')
			plt.savefig('collatzo_steps.png')

		plt.xlabel('Natural numbers')

	return


if __name__ == '__main__':

	plot_collatzo(x=5000, y=1000, inverse=True)