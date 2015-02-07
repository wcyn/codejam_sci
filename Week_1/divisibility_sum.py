"""Challenge A: (Divisibility sum)
If we list all the natural numbers 
below 10 that are multiples of 5 or 7,
we get 5 and 7. The sum of these multiples 
is 12. Find the sum of all the multiples of
7 and 11 below 10000.

[source: Project Euler(modified)]
"""

def div_sum(num):
	sum1 = 0
	while num > 0:
		if num % 7 == 0 and num % 11 == 0:
			sum1 += num
		num -= 1				
	print sum1 
div_sum(10000)