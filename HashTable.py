'''
Overview:
Literally a Dictionary.
Works by hashing keys.
Hashing is running data through a hash function that returns a memory address.
A hash is one-way and deterministic (same value is always the same hash)
Collisions result in two pairs sharing the same position in a nested list or linked list
	Called Seperate Chaining
Another option is to keep going down until you find an empty space
	Called Linear Probing (form of Open Addressing)
'''


class HashTable:
	def __init__(self, size=7):
		self.data_map = [None] * size

	def __hash(self, key):
		my_hash = 0
		for letter in key:
			my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
		return my_hash

	def print_table(self):
		for i, val in enumerate(self.data_map):
			print(i, ": ", val)

	def set_item(self, key, value):
		index = self.__hash(key)
		if self.data_map[index] is None:
			self.data_map[index] = []
		temp = 0
		added = False
		while not added and temp < len(self.data_map[index]):
			if self.data_map[index][temp][0] == key:
				self.data_map[index][temp][1] = value
				added = True
			else:
				temp += 1
		if not added:
			self.data_map[index].append([key, value])

	def get(self, key):
		index = self.__hash(key)
		if self.data_map[index]:
			for i in self.data_map[index]:
				if i[0] == key:
					return i[1]
		return None

	def keys(self):
		all_keys = []
		for i in self.data_map:
			if i:
				for j in i:
					all_keys.append(j[0])
		return all_keys
