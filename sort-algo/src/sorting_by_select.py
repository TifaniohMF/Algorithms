# Sorting algorithm by select

def sort_select(T):
	n = len(T)
	for i in range(1, n):
		key = T[i]
		j = i - 1
		# Move element in table T, which are bigger to the right
		while j >= 0 and key < T[j]:
			T[j+1] = T[j]
			j -= 1
		T[j+1] = key
	return T
