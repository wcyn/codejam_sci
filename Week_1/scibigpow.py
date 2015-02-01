"""Challenge C : (Sci Big Pow)
3 and 2 are the highest powers of
2 and 3 respectively that can give a 
result less than 10 i.e  2^3(8), 3^2(9). 
We shall call these highest powers scibigpow. 
The product of the factorials of these scibigpow 
is 3! * 2! = 12. Find the last 12 digits of the product 
of the factorials of the scibigpow of all numbers below 
1000 that give a result  less than the largest prime below 
2 billion
Note: (1^n = 1 and therefore we don't include 1 in the range 
of numbers)
[source: Sci CodeJam team]
"""
import math

def is_prime(num):
	if num <= 1 or num % 2 == 0:
		return 0 # don't bother checking the even numbers
	check = 3
	maxneeded = num
	while check < maxneeded + 1:
		maxneeded = num / check
		if num % check == 0:
			return 0
		check += 2
	return 1

def largest_prime(num):
	#return largest prime number below num.
	num -= 1 #less than num
	while not is_prime(num):
		# print "this ",num, " ain't prime"
		num -= 1
	return num

#scibigpow of all numbers below rangenum
def scibigpow(resultnum, rangenum = False):
	x = 2 #excluding 1
	power = 2 #no point starting at power of 1
	sci_prod = 1
	if not rangenum: #rangenum is False
		rangenum = resultnum
	while x < rangenum:
		pownum = x ** power 
		if pownum > resultnum:
			scibigpow = power - 1
			sci_prod *= math.factorial(scibigpow) 
			power = 2 #reset power 
			x += 1
		else:
			power += 1
	print "product ->", sci_prod
	print "last 12 digits -> ", str(sci_prod)[-12:]

scibigpow(largest_prime(2000000000),1000)



				