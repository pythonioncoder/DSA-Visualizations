'''
Overview:
Edges connecting Verticies (basically nodes)
Basically drawing a polygon.
You can also have weighted edges (like NN)
Or Directional/Bidirectional edges

Trees are a form of a graph, with a limitation of only 2 edges per node
Linked Lists are a form of a graph with only one edge per node

Adjacency Matrix:
Bidirectional graphs are mirrored along the main diagonal.
Main diagonal is always 0 because no vertex can have an edge with itself.
Weights can be stored in the matrix with the edges

Adjacency List:
{
'A': ['B', 'E'],  <-- Vertex A has edges with B and E
'B': ['A', 'C'],
.
.
.
}

Big O:
Space: 							O(n^2) Matrix, O(V + E)
Adding a Vertex w/o edges: 		Add a new row/column O(V^2) Matrix, O(1) List
Add an edge:					O(1) Matrix, O(1) List
Remove an edge:					O(1) Matrix, O(E) List to find each edge in the edge list
Remove a vertex:				O(V^2) to remove row and column Matrix, O(V + E) List because you need to change every vertex list
'''


class Graph:
	def __init__(self):
		self.adj_list = {}

	def print_graph(self):
		for vertex in self.adj_list:
			print(vertex, ": ", self.adj_list[vertex])

	def add_vertex(self, vertex):
		if vertex not in self.adj_list:
			self.adj_list[vertex] = []
			return True
		return False

	def add_edge(self, v1, v2):
		if v1 in self.adj_list and v2 in self.adj_list:
			self.adj_list[v1].append(v2)
			self.adj_list[v2].append(v1)
			return True
		return False

	def remove_edge(self, v1, v2):
		if v1 in self.adj_list and v2 in self.adj_list:
			try:
				self.adj_list[v1].remove(v2)
				self.adj_list[v2].remove(v1)
			except ValueError:
				return False
			return True
		return False

	def remove_vertex(self, vertex):
		# You can remove edges specified in dict bc bidirectional
		if vertex in self.adj_list:
			for other_vertex in self.adj_list[vertex]:
				self.adj_list[other_vertex].remove(vertex)
			del self.adj_list[vertex]
			return True
		return False
