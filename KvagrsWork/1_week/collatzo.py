#!/usr/bin/env python

import matplotlib
import pylab as plt

def collSteps(n, maxNumber=False):
	steps 	= 0
	maxN 	= n
	while n != 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = 3 * n + 1
		steps += 1
		maxN = max(maxN, n)
	if maxNumber:
		return maxN
	else:
		return steps


def plotCollatzo(x=8000, y=300, maxNumber=False, filename=''):


	points=[]
	plt.axis([0,x,0,y])
	for i in range(1,x):
		points.append(collSteps(i, maxNumber))
		
	if maxNumber:	
		plt.plot( range(1, x), points, 'ko' )		# collSteps(i)[1] for max
		plt.ylabel('Maximal number aj')
		plt.savefig('img/' + filename + '.png')
	else:
		plt.plot( range(1, x), points, 'ko' )		# collSteps(i)[0] for steps
		plt.ylabel('Number of steps')
		plt.savefig('img/' + filename + '.png')

	return


if __name__ == '__main__':

	plotCollatzo(x=25, y=25, filename="collatzo_steps_25")
	plotCollatzo(x=8000, y=300, filename="collatzo_steps_8000")
	plotCollatzo(x=5000, y=5000, maxNumber=True, filename="collatzo_max")