'''
Function tangent implementation 
'''

from src.sin import *
from src.cos import *

class tangent(object):
	def __init__(self, angle):
		self.angle = angle
	
	def tan(angle, in_degrees=False):
	   s = sinus.sin(angle, in_degrees)
	   c = cosinus.cos(angle, in_degrees)
	   if c == 0:
	   	return float('inf')
	   return  (s / c)