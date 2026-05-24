'''
This program représente the sum list
'''
from math_lib.src.sqrt import *

class Stats(object):
	def __init__(self, L):
		self.L = L
		
	def sum(L):
		S = 0
		n = len(L)
		for i in range(n):
			S += L[i]
		return S
	
	def mean(L):
		S = 0
		n = len(L)
		for i in range(n):
			S += L[i]
			moy = S/n
		return moy
	
	def var(L):
		S = 0
		n = len(L)
		for i in range(n):
			S += L[i]**2
			var = S/n - Stats.mean(L)**2
		return var
	
	def ecart(L):
		return Sqrt.sqrt(Stats.var(L))