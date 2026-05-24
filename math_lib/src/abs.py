'''
In this program, I write the absolute value 
For a number
>> abs(-34) == 34

To find a max absolute value in a list
>> absMax([1,2,3,-12]) == -12

To find a min absolute value in a list
>> absMin([-1,2,3,-12]) == -1
'''

class absolute(object):
	def __init__(self, number, list):
		self.number = number
		self.list = list
	def abs(number):
	           if number > 0:
	           	return number
	           else:
	           	return -number
	def absMax(list):
	    j = list[0]
	    for i in list:
	    	if abs(i) > abs(j):
	    		j = i
	    return j
	def absMin(list):
	     j = list[0]
	     for i in list:
	      	if abs(i) < abs(j):
			      j = i
	     return j