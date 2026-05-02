def fact(n):
	M = 1
	for i in range(0, n):
		M *= (n-i)
	return M