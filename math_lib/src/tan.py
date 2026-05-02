'''
Function tangent implementation 
'''

from sin import sin
from cos import cos

def tan(angle, in_degrees=False):
    s = sin(angle, in_degrees)
    c = cos(angle, in_degrees)
    if c == 0: 
        return float('inf')
    return  (s / c)