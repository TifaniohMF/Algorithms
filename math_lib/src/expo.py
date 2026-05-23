'''
Exponential function implementation 
'''
from src.factorial import *
class expo:
	def exp(x):
		# x expo(x)
		f=100 # max iteration
		S = 0
		for i in range(f+1):
			S+= (x**i)/facto.fact(i)
		return S