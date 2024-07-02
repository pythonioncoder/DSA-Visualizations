'''
Overview:
Stacks are like a stack of books.
Add an item onto the stack - Push
You can only reach the last item pushed
Removing last added item - Pop
LIFO - Last In First Out

Benefits:
	O(1) to Push/Pop

Examples:
	Browser History (Back Button)
	Recursion

Implementation:
	List
	Linked List
	Stack should point down so popping/pushing the top value is O(1)
		without needing to find the second last node
'''


class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Stack:
	def __init__(self, value):
		new_node = Node(value)
		self.top = new_node
		self.height = 1

	def print_stack(self):
		temp = self.top
		while temp is not None:
			print(temp.value)
			temp = temp.next

	def push(self, value):
		# O(1)
		new_node = Node(value)
		if self.top is None:
			self.top = new_node
		else:
			new_node.next = self.top
			self.top = new_node
		self.height += 1

	def pop(self):
		if self.top is None:
			return None
		temp = self.top
		self.top = self.top.next
		temp.next = None
		self.height -= 1
		return temp
