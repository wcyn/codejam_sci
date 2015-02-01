"""Challenge B: (Divisibility Sum – Modified)
The numbers below 100 that are divisible by
all primes below 7 are: 30, 60 and 90. Their
sum is 180. Find the sum of all odd  numbers
below 100,000 that are divisible by all primes
p for 2<p<10

[source: Project Euler (modified)]
"""

#primes 3, 5, 7
#LCM = 3*5*7 = 105

LCM = 3 * 5 * 7

def div_sum_prime(num):
	sum1 = 0
	while num > 0:
		if num % 2 != 0 and num % LCM == 0:
			sum1 += num
		num -= 1
	print sum1
				
div_sum_prime(1000)