def selection_sort(unsorted):
	for i in range(len(unsorted) - 1):
		min_index = i
		for j in range(i + 1, len(unsorted)):
			if unsorted[j] < unsorted[min_index]:
				min_index = j

		if i != min_index:
			temp = unsorted[i]
			unsorted[i] = unsorted[min_index]
			unsorted[min_index] = temp

	return unsorted
