'''
Exponential function implementation 
This implementation use DL :
	exp(x) := \sum_{k=0}^{n} x^{k}/k!
'''
from src.factorial import *

class expo:
	def __init__(self, x):
		self.x = x
	
     # Exponential value 	
	def exp(self):
		f=100 # max iteration
		S = 0
		for i in range(f+1):
			S+= (self.x**i)/factorial(i).fact()
		return S
