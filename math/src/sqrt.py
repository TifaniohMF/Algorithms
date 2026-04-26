'''
In this program, I programmed the square Root of number.
'''

def sqrt(n):
	try:
		return n**(1/2)
	except ValueError:
		print("Math domain error")
		
def sqrt3(n):
	try:
		return n**(1/3)
	except ValueError:
		print("Math domain error")