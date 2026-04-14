# In this program, I implement the fibonacci algorithm 

def multiplication(A, B): # function which calculate two matrix 2 x 2
	C = [[0,0], [0,0]] 
	for i in range(2):
		for j in range(2):
			for k in range(2):
				C[i][j] += A[i][k]*B[k][j]
	return C 
	
def puissance_mat(A, n): # function which calculate matrix in pow n
	res = [[1, 0], [0, 1]]
	while n > 0:
		if n % 2 == 1:
			res = multiplication(res, A)
		A = multiplication(A, A)
		n //= 2
	return res
	
def fibonacci(n):
	if n == 0 : return 0
	elif n == 1 : return 1
	T = [[1, 1], [1, 0]]
	T_n = puissance_mat(T, n-1)
	
	return T_n[0][0] # the n-th fibonacci number is in top left to n-th matrix