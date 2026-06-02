'''
In this program, I create to allows calculate a power of numbers
'''
class Pow:
	def __init__(self, x, n):
		self.x = x
		self.n = n
		
	def power(self):
		if self.n == 0:
			return 1
		else:
			if self.n % 2 == 0:
				return Pow(self.x*self.x, self.n/2).power()
			else:
				return self.x*Pow(self.x*self.x, (self.n-1)/2).power()
