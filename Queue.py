'''
Overview:
FIFO - First In First Out
People in Queue = En Queue
Remove People = De Queue

Implementation:
	Remove and Add on either end (First/Last)
	List
		One end is O(1) other is O(n) because of re-indexing
	Linked List
		Removing on one end is O(n) because of traversal,
			but everything else is O(1)
		Therefore, you want to only En-queue from Last
			and de-queue from First
'''


class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Queue:
	def __init__(self, value):
		new_node = Node(value)
		self.first = new_node
		self.last = new_node
		self.length = 1

	def print_queue(self):
		temp = self.first
		while temp is not None:
			print(temp.value)
			temp = temp.next

	def enqueue(self, value):
		new_node = Node(value)
		if self.first is None:
			self.first = new_node
			self.last = new_node
		else:
			self.last.next = new_node
			self.last = new_node
		self.length += 1

	def dequeue(self):
		if self.first is None:
			return None
		temp = self.first
		if self.length == 1:
			self.first = None
			self.last = None
		else:
			self.first = temp.next
			temp.next = None
		self.length -= 1
		return temp
