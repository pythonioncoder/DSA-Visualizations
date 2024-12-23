def merge_sort(unsorted):
	if len(unsorted) < 2:
		return unsorted

	left = unsorted[:len(unsorted)//2]
	right = unsorted[len(unsorted)//2:]
	result = []

	left = merge_sort(left)
	right = merge_sort(right)

	while len(left) > 0 and len(right) > 0:
		if left[0] < right[0]:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
	result += left
	result += right

	return result
