# Sorting algortithms by replacement

def sort_replacement(T):
	n = len(T)
	A = [0]*n
	
	for i in range(n):
		# Tof find minimum
		min_val = float('inf')
		min_index = -1
		for j in range(n):
			if T[j] < min_val:
				min_val = T[j]
				min_index = j
		
		# Copy minimum in a table empty
		A[i] = min_val
		
		# Replace minimum by maximum in table T
		T[min_index] = max(T)
	return A
