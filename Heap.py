'''
Overview:
BST with Highest value is always at the top
Complete Tree - Horizontal Line without gaps
Equal values can be below

Min heaps are opposite of Max heaps (described above)
Height is log(n)

Order is not preserved other than a general trend top-bottom

Stored in a List
Able to figure out when one layer ends and next begins because each node
	only has two children
Because of that, you can calculate the positions of children IF you start
	at index one

left_child = 2 * parent_index
right_child = 2 * parent_index + 1
parent = left_child / 2
parent = right_child // 2
just use // for any node

Insert - Add value to next available node in the last layer to keep
		the tree complete, bubble it up to the highest node possible
'''


class MaxHeap:
	def __init__(self):
		self.heap = []

	def _left_child(self, index):
		return 2 * index + 1

	def _right_child(self, index):
		return 2 * index + 2

	def _parent(self, index):
		return (index - 1) // 2

	def _swap(self, index1, index2):
		self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

	def insert(self, value):
		self.heap.append(value)
		current = len(self.heap) - 1
		while self.heap[self._parent(current)] < self.heap[current] and current > 0:
			self._swap(current, self._parent(current))
			current = self._parent(current)
		return True

	def _sink_down(self, index):
		max_index = index
		while True:
			left_index = self._left_child(max_index)
			right_index = self._right_child(max_index)

			if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
				max_index = left_index

			if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
				max_index = right_index

			if max_index != index:
				self._swap(index, max_index)
				index = max_index
			else:
				return

	def remove(self):
		if len(self.heap) == 0:
			return None
		if len(self.heap) == 1:
			return self.heap.pop()
		max_value = self.heap[0]
		self.heap[0] = self.heap.pop(-1)
		self._sink_down(0)

		return max_value


mh = MaxHeap()
mh.insert(95)
mh.insert(75)
mh.insert(80)
mh.insert(55)
mh.insert(60)
mh.insert(50)
mh.insert(65)
print(mh.heap)
mh.remove()
print(mh.heap)
mh.remove()
print(mh.heap)
