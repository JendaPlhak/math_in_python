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


def plot_collatzo(x=8000, y=300, maxNumber=False):

	points=[]
	plt.axis([0,x,0,y])
	for i in range(1,y):
		points.append([i, collSteps(i)])
		
		if maxNumber:
			plt.plot( [i],[collSteps(i)[1]], 'ko' )				# collSteps(i)[0] are steps, collSteps(i)[1] are max num in collatzo series
			plt.ylabel('Number of steps')
			plt.savefig('collatzo_max.png')

		else:
			plt.plot( [i],[collSteps(i)[0]], 'ko' )
			plt.ylabel('Number of steps')
			plt.savefig('collatzo_steps.png')

	return


if __name__ == '__main__':

	plot_collatzo()