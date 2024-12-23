import statistics


def quick_sort(unsorted):
	if len(unsorted) < 2:
		return unsorted

	pivot = statistics.median([unsorted[0], unsorted[len(unsorted)//2], unsorted[-1]])
	i = -1
	j = len(unsorted)
	while True:
		i += 1
		j -= 1
		while unsorted[i] < pivot:
			i += 1
		while unsorted[j] > pivot:
			j -= 1

		if j <= i:
			break

		temp = unsorted[i]
		unsorted[i] = unsorted[j]
		unsorted[j] = temp

	return quick_sort(unsorted[:i]) + quick_sort(unsorted[i:])
