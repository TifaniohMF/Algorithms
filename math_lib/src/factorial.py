'''
Factorial implementation 
'''
class facto(object):
	def __init__(self, n):
		self.n = n
		
	def fact(n):
		M = 1
		for i in range(0, n):
			M *= (n-i)
		return M