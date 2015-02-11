"""
Challenge B: (Cubic permutations)
The cube, 41063625 (345^3), can be 
permuted to produce two other cubes:  
56623104 (384^3) and 66430125 (405^3). 
In fact, 41063625 is the smallest cube 
which has exactly three permutations of 
its digits which are also cube. Find the 
largest cube for which exactly five permutations 
of its digits are cube.
[Source: Project Euler(modified) problem 62]

"""

cubes = {}
def cubic_permutation(perm_no):
	for i in xrange(10000):
		j = i ** 3
		num = "".join(sorted(str(j)))
		# print "j: ",j
		# print "num: ",num

		if cubes.has_key(num):
			# print "cubes[num] ",cubes[num]
			cubes[num].append(j)
			if len(cubes[num]) == perm_no:
				print min(cubes[num])
				break
		else:
			cubes[num] = [j]
		
cubic_permutation(5)