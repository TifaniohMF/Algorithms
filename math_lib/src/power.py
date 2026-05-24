'''
In this program, I create to allows calculate a power of numbers
'''
class Pow(object):
	def __init__(self, x, n):
		self.x = x
		self.n = n
		
	def power(x, n):
		if n == 0:
			return 1
		else:
			if n % 2 == 0:
				return Pow.power(x*x, n/2)
			else:
				return x*Pow.power(x*x, (n-1)/2)