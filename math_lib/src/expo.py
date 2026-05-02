'''
Exponential function implementation 
'''
from src.factorial import fact
def exp(x):
	# x expo(x)
	f=100 # max iteration
	S = 0
	for i in range(f+1):
		S+= (x**i)/fact(i)
		
	return S
	
print(exp(5))