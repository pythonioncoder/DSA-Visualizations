import matplotlib.pyplot as plt
import numpy as np


class Vis:
	def __init__(self, a=100, barcol='white'):
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


def merge_sort(current: Vis, lo, hi):
	unsorted = current.lst[lo:hi]

	if len(unsorted) < 2:
		return unsorted

	left = merge_sort(current, lo, lo + round(len(unsorted)/2)).copy()
	right = merge_sort(current, lo + round(len(unsorted)/2), hi).copy()

	l, r = 0, 0
	while l < len(left) and r < len(right):
		if left[l] < right[r]:
			current.lst[lo+l+r] = left[l]
			l += 1
			current.highlights[lo+l+r] = 'green'
			current.display()
			current.highlights[lo + l + r] = current.barcol
		else:
			current.lst[lo+l+r] = right[r]
			r += 1
			current.highlights[lo + l + r] = 'green'
			current.display()
			current.highlights[lo + l + r] = current.barcol

	if l < len(left):
		for i in range(len(left[l:])):
			current.lst[lo+l+r+i] = left[l+i]
			current.highlights[lo + l + r] = 'green'
			current.display()
			current.highlights[lo + l + r] = current.barcol
	elif r < len(right):
		for i in range(len(right[r:])):
			current.lst[lo+l+r+i] = right[r+i]
			current.highlights[lo + l + r] = 'green'
			current.display()
			current.highlights[lo + l + r] = current.barcol

	return current.lst[lo:hi]
