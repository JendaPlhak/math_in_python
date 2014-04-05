#!/usr/bin/env python

def sieveOfEratosthenes(n):

	numbers = [True] * n
	i = 2
	while i**2 < n:
		for j in range(2,int(n/i)+1):
			numbers[(i*j)-1] = False

		i += 1

	primes = []
	for j in range(1,n):
		if numbers[j] == True:
			primes.append(j+1)

	return primes

	
if __name__ == '__main__':

	sieveOfEratosthenes(1000)