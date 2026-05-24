'''
Function cosinus implementation 
'''
class cosinus(object):
    def __init__(self, angle):
    	self.angle = angle
    	
    def cos(angle, in_degrees=False): # in_degrees = degre
    	# 1.  Pi (approximation)
    	PI = 3.141592653589793
    	
    	# 2. Conversion
    	x = angle * (PI / 180) if in_degrees else angle
    	
    	#3. Angle radian
    	x = x % (2 * PI)
    	
    	# 4. Calcul by Taylor series optimised
    	S = 1.0 
    	terme = 1.0
    	f = 20
    	for i in range(1, f + 1):
    	    terme *= -x**2 / ((2*i - 1) * (2*i))
    	    S += terme
    	return S