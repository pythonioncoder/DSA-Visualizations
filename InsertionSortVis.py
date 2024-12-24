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


def insertion_sort(current_vis: Vis):
	unsorted = current_vis.lst
	for i in range(1, len(unsorted)):
		j = i-1
		current = unsorted[j+1]
		while current < unsorted[j] and j > -1:
			unsorted[j+1] = unsorted[j]
			unsorted[j] = current
			j -= 1
			current_vis.highlights[j] = 'green'
			current_vis.display()
			current_vis.highlights[j] = current_vis.barcol

	return unsorted


if __name__ == '__main__':
	my_vis = Vis()
	insertion_sort(my_vis)
