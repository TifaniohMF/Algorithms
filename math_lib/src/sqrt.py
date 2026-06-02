'''
In this program, I programmed the square Root of number.
'''
class Sqrt:
	def __init__(self, n):
		self.n = n
	
	# Sqrt value 
	def sqrt(self):
		try:
			return self.n**(1/2)
		except ValueError:
			print("Math domain error")
			
	# Sqrt 3-rd value
	def sqrt3(self):
		try:
			return self.n**(1/3)
		except ValueError:
			print("Math domain error")
