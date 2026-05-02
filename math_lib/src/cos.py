'''
Function cosinus implementation 
'''
def cos(angle, in_degrees=False): # in_degrees = degre
    # 1.  Pi (approximation)
    PI = 3.141592653589793
    
    # 2. Conversion
    x = angle * (PI / 180) if in_degrees else angle
    
    # 3. Angle reduct (Modulo 2*PI)
    x = x % (2 * PI)
    
    # 4. Calcul par série de Taylor optimisée
    S = 1.0 
    terme = 1.0
    f = 20     
    
    for i in range(1, f + 1):
        terme *= -x**2 / ((2*i - 1) * (2*i))
        S += terme
        
    return S

print(cos(5, in_degrees=True))