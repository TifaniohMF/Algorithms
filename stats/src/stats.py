'''
This program représente the sum list
'''
from math_lib.src.sqrt import *

class Stats:
	def __init__(self, L):
		self.L = L
		
	def sum(self):
		S = 0
		n = len(self.L)
		for i in range(n):
			S += self.L[i]
		return S
	
	def mean(self):
		S = 0
		n = len(self.L)
		for i in range(n):
			S += self.L[i]
			moy = S/n
		return moy
	
	def var(self):
		S = 0
		n = len(self.L)
		for i in range(n):
			S += self.L[i]**2
			var = S/n - Stats(self.L).mean()**2
		return var
	
	def ecart(self):
		return Sqrt(Stats(self.L).var()).sqrt()
