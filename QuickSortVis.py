import matplotlib.pyplot as plt
import numpy as np


class Vis:
	def __init__(self, a=100, barcol='white'):
		self.amount = a
		self.barcol = barcol
		self.lst = []
		self.x = np.arange(0, self.amount, 1)
		self.highlights = np.full(self.amount, barcol)
		self.end = False

		vals = np.arange(self.amount)
		for i in vals:
			x = np.random.randint(0, len(vals))
			self.lst.append(vals[x])
			vals = np.delete(vals, x)
		self.lst = np.array(self.lst)

	def display(self):
		if self.end:
			plt.close()
			return
		plt.clf()
		plt.gcf().set_facecolor('black')
		plt.bar(self.x, self.lst, color=self.highlights)
		plt.axis('off')
		plt.pause(0.0001)


def _quick_sort(current: Vis, lo, hi):
	unsorted = current.lst[lo:hi]

	if len(unsorted) < 2:
		return unsorted

	pivot = np.median([unsorted[0], unsorted[len(unsorted)//2], unsorted[-1]])
	if pivot == unsorted[0]:
		pivot_index = 0
	elif pivot == unsorted[-1]:
		pivot_index = len(unsorted)-1
	else:
		pivot_index = len(unsorted)//2
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

		current.highlights[lo+i], current.highlights[lo+j], current.highlights[lo+pivot_index] = 'green', 'green', 'red'
		current.display()

		temp = unsorted[i]
		unsorted[i] = unsorted[j]
		unsorted[j] = temp

		current.display()
		current.highlights[lo+i], current.highlights[lo+j], current.highlights[lo+pivot_index] = current.barcol, current.barcol, current.barcol

	res = _quick_sort(current, lo, lo+i) + _quick_sort(current, lo+i, hi)

	if lo == 0 and hi == len(current.lst):
		current.end = True
		current.display()

	return res


def quick_sort(current: Vis):
	return _quick_sort(current, 0, len(current.lst))


if __name__ == '__main__':
	my_vis = Vis()
	quick_sort(my_vis)
