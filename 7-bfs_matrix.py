# Python3 implementation of the approach
class Graph:
	
	adj = []

	# Function to fill empty adjacency matrix
	def __init__(self, v, e):
		
		self.v = v
		self.e = e
		Graph.adj = [[0 for i in range(v)]
						for j in range(v)]

	# Function to add an edge to the graph
	def addEdge(self, start, e):
		
		# Considering a directional edge
		Graph.adj[start][e] = 1
		#Graph.adj[e][start] = 1

	# Function to perform DFS on the graph
	def DFS(self, start, visited):
		
		# Print current node
		print(start, "-->", end = ' ')

		# Set current node as visited
		visited[start] = True

		# For every node of the graph
		for neighbor in range(self.v):
			
			# If some node is adjacent to the current node and it has not already been visited
			if (Graph.adj[start][neighbor] == 1 and (not visited[neighbor])):
				self.DFS(neighbor, visited)

#set node and edge
v, e = 8, 8

# Create the graph
G = Graph(v, e)

G.addEdge(1, 2)
G.addEdge(2, 7)
G.addEdge(2, 4)
G.addEdge(3, 4)
G.addEdge(4, 6)
G.addEdge(5, 4)
G.addEdge(5, 3)
G.addEdge(7, 5)

# Visited vector to so that a vertex
# is not visited more than once
# Initializing the vector to false as no
# vertex is visited at the beginning
visited = [False] * v


# Perform DFS
G.DFS(1, visited);


