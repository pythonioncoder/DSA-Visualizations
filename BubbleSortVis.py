import matplotlib.pyplot as plt
import numpy as np


class Vis:
	def __init__(self, a=50, barcol='white'):
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


def bubble_sort(current: Vis):
	unsorted = current.lst
	for i in range(len(unsorted) - 1, 0, -1):
		for j in range(i):
			if unsorted[j] > unsorted[j + 1]:  # Swaps the two
				temp = unsorted[j + 1]
				unsorted[j + 1] = unsorted[j]
				unsorted[j] = temp
				current.highlights[j] = 'green'
				current.display()
				current.highlights[j] = current.barcol

	current.end = True
	current.display()

	return unsorted


if __name__ == '__main__':
	my_vis = Vis()
	bubble_sort(my_vis)
