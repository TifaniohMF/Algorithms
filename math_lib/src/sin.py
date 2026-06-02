'''
Function sinus implementation 
'''
class sinus:
	def __init__(self, data):
		self.angle = data if isinstance (data, (int, float)) else None
	
	def sin(self, in_degrees=False):
	   # 1.  Pi (approximation)
	   PI = 3.141592653589793
	   
	   # 2. Conversion
	   x = self.angle * (PI / 180) if in_degrees else self.angle
	   
	   # 3. Angle reduct (Modulo 2*PI)
	   x = x % (2 * PI)
	   
	   # 4. Calcul par série de Taylor optimisée
	   S = x
	   terme = x
	   f = 20     
	   
	   for i in range(1, f + 1):
	       terme *= -x**2 / ((2*i) * (2*i + 1))
	       S += terme
	   return S
