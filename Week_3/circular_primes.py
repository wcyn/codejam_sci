"""
Challenge B (Circular primes)
The number, 197, is called a circular 
prime because all rotations of the digits: 
197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 
and 97. The Fibonacci equivalent is Fibonacci(13) = 377
Find the Fibonacci equivalent of circular primes below 
one million.
[source: {project euler}(modified)]

"""

import time,math
from collections import deque
start = time.clock()

def get_rotations(num):
	string_num = str(num)
	rotations = []
	for i in range(len(string_num)):
		rotations.append(int(string_num[i:] + string_num[0:i]))	
	return rotations

def eratosthenes_sieve(num):
	if num<=2:
		return []
	sieve = range(3,num,2)
	top = len(sieve)
	for i in sieve:
		if i:
			bottom = (i * i - 3) // 2
			if bottom >= top:
				break
			sieve[bottom::i] = [0] * -((bottom - top) // i)
	return [2] + [j for j in sieve if j]

def fib(num):
	if num+1==0: return 0
	elif num+1==1: return 1
	else: return fib(num-1) + fib(num-2)

def get_circular_primes_fib(num):
	#get circular primes below num
	primes = eratosthenes_sieve(num)
	circular_primes = []
	for i in primes:
		test = True
		for j in get_rotations(i):
			if j % 2 == 0 or j not in primes:
				test = False
				break
		if test:
			circular_primes.append(i)
	return fib(len(circular_primes))

print get_circular_primes_fib(10000) #this is the computation 
									 #that can be done within reasonable time frame
									 # (2.5 seconds)

end = time.clock() - start
print end
