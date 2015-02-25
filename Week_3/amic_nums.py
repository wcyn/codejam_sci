"""
Challenge A (Amicable numbers)
Let d(n) be defined as the sum of
proper divisors of n (numbers less 
than n which divide evenly into n). 
If d(a) = b and d(b) = a, where a != b, 
then a and b are an amicable pair and 
each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 
2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore 
d(220) = 284. The proper divisors of 284 are 1, 2, 
4, 71 and 142; so d(284) = 220.
Evaluate the product of all the amicable numbers 
under 10000.
[source: {project euler} (modified)]

"""
import time, math
start_time = time.clock()

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

def prop_divs(num):
	x = 1
	divs = []
	if is_prime(num):
		return [1]

	while num/2 >= x:
		if num % x == 0: divs.append(x)
		x+=1
	return divs

def amicable_nums(num):
	# get amicable numbers below num
	amic_pairs = []
	x = 2
	while x < num:
		j = 2
		if not is_prime(x):
			while j < x/3:
				if not is_prime(x+j):
					if sum(prop_divs(x)) == x+j and sum(prop_divs(x+j)) == x:
						amic_pairs.append((x,x+j))
				j+=1
		x+=1
	print amic_pairs


prop_start = time.clock()
amicable_nums(300) # this takes a reasonable amount of time to complete. 
				   # Beyond that, it's very inefficient
# amicable_nums(2000) #just this takes 64 seconds to compute :(
prop_end = time.clock() - prop_start
print prop_end
print ("-- %s seconds --" % str(time.clock() - start_time))
