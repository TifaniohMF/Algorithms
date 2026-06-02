'''
Factorial implementation 
'''
class factorial:
	def __init__(self, n):
		self.n = n 
	
    # Factorial value
	def fact(self):
		M = 1
		for i in range(0, self.n):
			M *= (self.n - i)
		return M
