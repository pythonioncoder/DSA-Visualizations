'''
Overview:
Linked List is a non-forking tree

Binary Tree = Node with 2 other nodes branching off
Full Tree = Node with every node either pointing to 0 or 2 nodes
Perfect Tree = Any level is completely filled all the way across
Complete Tree = Filled tree, left-to-right, with no gaps

Parent Node - Child Node
1 Parent for a node
Leaf = Childless Nodes

Binary Search Tree = Start at parent node, if larger value, go right, smaller, go left.
					compare with each child node until at leaf.
As the tree grows, nodes = 2^levels - 1
Takes O(log(nodes)) = O(log n) steps to find/append/pop a particular node
Divide & Conquer because of left/right for lesser/greater
That's for most trees (Ideal case is Perfect Tree)

Worst Case, if tree never forks, all values on one side
It's a Linked List. O(n) lookup/insert/remove

Lookup: LL O(n), BST O(log n)
Remove: LL O(n), BST O(log n)
Insert: LL O(1), BST O(log n) cuz of traversal
LL is very quick with appending, no other DS beats it
'''


class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class BinarySearchTree:
	def __init__(self):
		self.root = None  # Empty Tree Initialization

	def insert(self, value):
		new_node = Node(value)
		if self.root is None:
			self.root = new_node
			return True
		temp = self.root
		while True:
			if value == temp.value:
				return False
			if value < temp.value:
				if temp.left:
					temp = temp.left
				else:
					temp.left = new_node
					return True
			else:
				if temp.right:
					temp = temp.right
				else:
					temp.right = new_node
					return True

	def contains(self, value):
		temp = self.root
		while temp:
			if temp.value == value:
				return True
			if value < temp.value:
				temp = temp.left
			else:
				temp = temp.right
		return False
