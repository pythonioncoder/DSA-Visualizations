def insertion_sort(unsorted):
	for i in range(1, len(unsorted)):
		j = i-1
		current = unsorted[j+1]
		while current < unsorted[j] and j > -1:
			unsorted[j+1] = unsorted[j]
			unsorted[j] = current
			j -= 1

	return unsorted
