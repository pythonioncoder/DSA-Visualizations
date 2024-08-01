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

	def __r_contains(self, current_node, value):
		if current_node is None:
			return False
		if value == current_node.value:
			return True
		if value < current_node.value:
			return self.__r_contains(current_node.left, value)
		else:
			return self.__r_contains(current_node.right, value)

	def r_contains(self, value):
		return self.__r_contains(self.root, value)

	def __r_insert(self, current_node, value):
		if current_node is None:
			return Node(value)
		if value < current_node.value:
			current_node.left = self.__r_insert(current_node.left, value)
		elif value > current_node.value:
			current_node.right = self.__r_insert(current_node.right, value)
		return current_node

	def r_insert(self, value):
		if self.root is None:
			self.root = Node(value)
		self.__r_insert(self.root, value)

	def min_value(self, current_node):
		while current_node.left is not None:
			current_node = current_node.left
		return current_node.value

	def __delete_node(self, current_node, value):
		if current_node is None:
			return None
		if value < current_node.value:
			current_node.left = self.__delete_node(current_node.left, value)
		elif value > current_node.value:
			current_node.right = self.__delete_node(current_node.right, value)
		else:
			if current_node.left is None and current_node.right is None:
				return None
			elif current_node.left is None:
				current_node = current_node.right
			elif current_node.right is None:
				current_node = current_node.left
			else:
				sub_tree_min = self.min_value(current_node.right)
				current_node.value = sub_tree_min
				current_node.right = self.__delete_node(current_node.right, sub_tree_min)
		return current_node

	def delete_node(self, value):
		self.root = self.__delete_node(self.root, value)

	def bfs(self):
		current_node = self.root
		queue = []
		results = []
		queue.append(current_node)
		while queue:
			current_node = queue.pop(0)
			results.append(current_node.value)
			if current_node.left:
				queue.append(current_node.left)
			if current_node.right:
				queue.append(current_node.right)
		return results

	def dfs_preorder(self):
		results = []

		def traverse(current_node):
			results.append(current_node.value)
			if current_node.left:
				traverse(current_node.left)
			if current_node.right:
				traverse(current_node.right)

		traverse(self.root)
		return results

	def dfs_postorder(self):
		pass


bst = BinarySearchTree()
bst.r_insert(47)
bst.r_insert(21)
bst.r_insert(76)
bst.r_insert(18)
bst.r_insert(27)
bst.r_insert(52)
bst.r_insert(82)
print(bst.dfs_preorder())
