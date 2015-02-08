"""
Challenge A: (Permuted Multiples)
It can be seen that the number, 125874,
and its double, 251748, contain exactly   
the same digits, but in a different order.
Find the smallest positive integer, x, such 
that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
[Source: Project Euler( problem 52)]

"""

nums = [2,3,4,5,6]

def compare_digits(numlist):
	#compare addition of digits
	array = []
	for num in numlist:
		array.append(set([int(i) for i in str(num)]))
	# print ("array %s" % array)
	#check if every element in array is equal
	return array[1:] == array[:-1] 

def permuted_mults(numlist):
	scalar = 1
	numlist_store = numlist
	while not compare_digits(numlist):
		#while the digits don't match
		scalar+=1
		numlist = [x*scalar for x in numlist_store]
		
	print "The multiples: ",numlist
	print "x -> ", scalar

permuted_mults(nums)