def bubble_sort(unsorted):
	for i in range(len(unsorted) - 1, 0, -1):
		for j in range(i):
			if unsorted[j] > unsorted[j + 1]:  # Swaps the two
				temp = unsorted[j + 1]
				unsorted[j + 1] = unsorted[j]
				unsorted[j] = temp

	return unsorted


print(bubble_sort([4, 2, 6, 5, 1, 3]))
