import matplotlib.pyplot as plt
import numpy as np


class Vis:
	def __init__(self, a=50, barcol='white'):
		self.amount = a
		self.barcol = barcol
		self.lst = []
		self.x = np.arange(0, self.amount, 1)
		self.highlights = np.full(self.amount, barcol)

		vals = np.arange(self.amount)
		for i in vals:
			x = np.random.randint(0, len(vals))
			self.lst.append(vals[x])
			vals = np.delete(vals, x)
		self.lst = np.array(self.lst)

	def display(self):
		plt.clf()
		plt.gcf().set_facecolor('black')
		plt.bar(self.x, self.lst, color=self.highlights)
		plt.axis('off')
		plt.pause(0.0001)


def selection_sort(current: Vis):
	unsorted = current.lst
	for i in range(len(unsorted) - 1):
		min_index = i
		for j in range(i + 1, len(unsorted)):
			if unsorted[j] < unsorted[min_index]:
				min_index = j
			current.highlights[min_index] = 'red'
			current.highlights[j] = 'green'
			current.display()
			current.highlights[min_index], current.highlights[j] = current.barcol, current.barcol

		if i != min_index:
			temp = unsorted[i]
			unsorted[i] = unsorted[min_index]
			unsorted[min_index] = temp

	return unsorted


if __name__ == '__main__':
	my_vis = Vis()
	selection_sort(my_vis)
