class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None


class DoublyLinkedList:
	def __init__(self, value):
		new_node = Node(value)
		self.head = new_node
		self.tail = new_node
		self.length = 1

	def print_list(self):
		temp = self.head
		while temp is not None:
			print(temp.value)
			temp = temp.next

	def append(self, value):
		new_node = Node(value)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			new_node.prev = self.tail
			self.tail = new_node
		self.length += 1
		return True

	def pop(self):
		if self.length == 0:
			return None
		temp = self.tail
		if self.length == 1:
			self.head = None
			self.tail = None
		else:
			self.tail = temp.prev
			self.tail.next = None
			temp.prev = None
		self.length -= 1
		return temp

	def prepend(self, value):
		new_node = Node(value)
		if self.length == 0:
			self.head = new_node
			self.tail = new_node
		else:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node
		self.length += 1
		return True

	def pop_first(self):
		if self.length == 0:
			return None
		temp = self.head
		if self.length == 1:
			self.head = None
			self.tail = None
		else:
			self.head = temp.next
			self.head.prev = None
			temp.next = None
		self.length -= 1
		return temp

	def get(self, index):
		if index < 0 or index >= self.length:
			return None
		if index < self.length / 2:
			temp = self.head
			for _ in range(index):
				temp = temp.next
		else:
			temp = self.tail
			for _ in range((self.length - 1) - index):
				temp = temp.prev
		return temp

	def set_value(self, index, value):
		temp = self.get(index)
		if temp:
			temp.value = value
			return True
		return False

	def insert(self, index, value):
		if index == 0:
			return self.prepend(value)
		elif index == self.length:
			return self.append(value)
		left = self.get(index - 1)
		if left:
			right = left.next
			new_node = Node(value)
			left.next = new_node
			new_node.prev = left
			new_node.next = right
			right.prev = new_node
			self.length += 1
			return True
		return False

	def remove(self, index):
		if index == 0:
			return self.pop_first()
		elif index == self.length - 1:
			return self.pop()
		temp = self.get(index)
		if temp:
			left = temp.prev
			right = temp.next
			left.next = right
			temp.prev = None
			temp.next = None
			right.prev = left
			self.length -= 1
			return temp
		return None
