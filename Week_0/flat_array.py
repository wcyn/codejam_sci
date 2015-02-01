"""
An array is said to be nested
if it contains at least one array 
as an element. Implement an algorithm 
with a function/method that takes in a 
nested array and gives the number of arrays 
and number of elements  in the form (A, E) as 
output where A is the number of arrays and E is 
the number of elements.

"""

list1 = [2,4,5, ['something'],['list'], [3,2,1], 'something else']

def flat_array(list_obj):
	list_count, elem_count = 0,0
	
	for i in list_obj:
		if type(i) is list:
			list_count +=1
		else:
			elem_count +=1
	print elem_count, " <- elem_count"
	print list_count, " <- list_count\n"
flat_array(list1)