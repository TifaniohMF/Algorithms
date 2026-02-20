# Sorting algorithm by bubbles

def sort_bubbles(T):
	n = len(T)
	for i in range(n):
		# Verify if there is an exchange
		exchange = False
		
		# The last i element has always sorted
		for j in range(0, n-i-1):
			if T[j] > T[j+1]:
				T[j], T[j+1] = T[j+1], T[j]
				exchange = True
		
		# if table is always sorted
		if not exchange:
			break
	return T
