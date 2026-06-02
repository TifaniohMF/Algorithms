'''
Function tangent implementation 
'''

from src.sin import *
from src.cos import *

class tangent:
	def __init__(self, angle):
		self.angle = angle
	
	def tan(self, in_degrees=False):
	   s = sinus(self.angle).sin(in_degrees=True)
	   c = cosinus(self.angle).cos(in_degrees=True)
	   if c == 0:
	   	return float('inf')
	   return  (s / c)
