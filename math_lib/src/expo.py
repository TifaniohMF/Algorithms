'''
Exponential function implementation 
'''
from src.factorial import *

class expo:
	def __init__(self, x):
		self.x = x
		
	def exp(self):
		# x expo(x)
		f=100 # max iteration
		S = 0
		for i in range(f+1):
			S+= (self.x**i)/factorial(i).fact()
		return S
