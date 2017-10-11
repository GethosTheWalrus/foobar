import sys
import Queue

# maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
# maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
# maze = [[0, 1], [1, 0]]
# maze = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#               [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#               [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#               [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
#         [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# maze = [[0,1,1,0,0],
# 		[0,1,0,1,0],
# 		[0,0,0,1,0],
# 		]
# maze = [[0,0,0,0,0],
# 		[1,1,1,1,1],
# 		[1,1,0,0,1],
# 		[0,0,1,0,0],
# 		]
# maze = [[0,1,1],
# 		[1,1,1],
# 		[0,0,0],
# 		]
# maze = [[0, 1, 1, 0, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0]]
# maze = [[0,0],
# 		[0,0],
# 		[0,0],
# 		[0,0],
# 		[0,0],
# 		[0,0],
# 		[0,0],
# 		[0,0],
# 		[0,0],
# 		[0,0]
# 		]
# maze = [[0,0,1],
# 		[0,0,1],
# 		[0,0,1],
# 		[0,1,1],
# 		[1,0,1,1],
# 		[0,0,0,0],
# 		[0,1,1,0,1],
# 		[1,1,1,0,0,0],
# 		]

# maze = [[0],
# 		[0, 1],
# 		[0, 0, 1],
# 		[0, 0, 0, 1],
# 		[0, 1, 0, 0, 1],
# 		[0, 1, 0, 0, 0, 1],
# 		[0, 0, 1, 1, 0, 0, 0],
# 		]

# maze = [[0, 0, 1, 1, 0, 0, 0],
# 		[0, 1, 0, 0, 0, 1],
# 		[0, 1, 0, 0, 1],
# 		[1, 0, 0, 1],
# 		[1, 0, 1],
# 		[0, 0],
# 		[0],
# 		]

# maze = [[0,1,1,1,1,0],
# 		[0,0,1],
# 		[0,1,0,0,0],
# 		[0],
# 		[0,1,0,0,0,0,0],
# 		[1,0,1,0],
# 		[1,0,0],
# 		[0,0],
# 		]

maze = [
   [0, 1, 0, 1, 0, 0, 0], 
   [0, 0, 0, 1, 0, 1, 0]
]

class Graph():

	def __init__(self, maze, saldo):
		self.maze = maze
		self.saldo = saldo
		self.rows = len(maze)
		self.columns = len(maze[0])

	def shortestDistanceToEnd(self):

		visited = Queue.Queue()
		# source = Node(0, 0, self.saldo, self.maze, self.maze[0])
		source = Node(0, 0, self.saldo, self.maze)
		visited.put(source)
		distance = {source: 1}

		while not visited.empty():

			node = visited.get()

			if node.rowNum == self.rows - 1 and node.colNum == self.columns - 1:
				return distance[node]

			for neighbor in node.getNeighbors():
				if neighbor not in distance.keys():
					distance[neighbor] = distance[node] + 1
					visited.put(neighbor)

		return sys.maxint

class Node:
	# def __init__(self, rowNum, colNum, saldo, maze, row):
	def __init__(self, rowNum, colNum, saldo, maze):
		self.rowNum = rowNum
		self.colNum = colNum
		self.saldo = saldo
		self.maze = maze
		# self.row = row

	def __hash__(self):
		return self.colNum ^ self.rowNum

	def __eq__(self, other):
		return self.rowNum == other.rowNum and self.colNum == other.colNum and self.saldo == other.saldo

	def getNeighbors(self):
		neighbors = []
		rowNum = self.rowNum
		colNum = self.colNum
		saldo = self.saldo
		maze = self.maze
		# row = self.row
		rowLimit = len(maze)
		colLimit = len(maze[0])

		#makes sure we are not going to go passed the left boundary
		if colNum > 0:

			#checks if the node to the left of the current node
			#is a wall
			isAWall = maze[rowNum][colNum - 1] == 1
			if isAWall:
				#checks if this node has the ability to break
				#through a wall
				if saldo > 0:
					#append a NEW node object to the array of neighbors for
					#this node. One of my problems with my old version was 
					#that each node was sharing a pool of references, so
					#when a new node had the same neighbor as a previous
					#node, it would overwrite all of its data, which was
					#causing the algorithm to think it could break through
					#a wall when it in fact could not
					# neighbors.append( Node(rowNum, colNum - 1, saldo, maze, maze[rowNum]) )
					neighbors.append( Node(rowNum, colNum - 1, saldo - 1, maze) )
			else:
				#append a NEW node object to the array of neighbors for
				#this node. One of my problems with my old version was 
				#that each node was sharing a pool of references, so
				#when a new node had the same neighbor as a previous
				#node, it would overwrite all of its data, which was
				#causing the algorithm to think it could break through
				#a wall when it in fact could not
				# neighbors.append( Node(rowNum, colNum - 1, saldo, maze, maze[rowNum]) )
				neighbors.append( Node(rowNum, colNum - 1, saldo, maze) )

		#makes sure we are not going to go passed the right boundary
		if colNum < colLimit - 1:

			#checks if the node to the right of the current node
			#is a wall
			isAWall = maze[rowNum][colNum + 1] == 1
			if isAWall:
				#checks if this node has the ability to break
				#through a wall
				if saldo > 0:
					neighbors.append( Node(rowNum, colNum + 1, saldo - 1, maze) )
			else:
				#same deal as the above 'if'
				# neighbors.append( Node(rowNum, colNum + 1, saldo, maze, maze[rowNum]) )
				neighbors.append( Node(rowNum, colNum + 1, saldo, maze) )

		#makes sure we are not going to go passed the top boundary
		if rowNum > 0:
			
			#makes sure we are not checking a value that does not exist
			#in the case that the matrix is not rectangular
			# if len(row) == len(maze[rowNum - 1]) or colNum < len(row) - abs(len(row) - len(maze[rowNum - 1])):

			#checks if the node on top of the current node
			#is a wall
			isAWall = maze[rowNum - 1][colNum] == 1
			if isAWall:
				#checks if this node has the ability to break
				#through a wall
				if saldo > 0:
					neighbors.append( Node(rowNum - 1, colNum, saldo - 1, maze) )
			else:
				#same deal as the above 'if'
				# neighbors.append( Node(rowNum - 1, colNum, saldo, maze, maze[rowNum]) )
				neighbors.append( Node(rowNum - 1, colNum, saldo, maze) )

		#makes sure we are not going to go passed the bottom boundary
		if rowNum < len(maze) - 1:

			#makes sure we are not checking a value that does not exist
			#in the case the the matrix is not rectangular
			# if len(row) > len(maze[rowNum + 1]):
			# 	colLimit = len(maze[rowNum + 1]) - 1
			# else:
			# 	colLimit = len(row) - abs(len(row) - len(maze[rowNum + 1]))
			# 	if colLimit < 0:
			# 		colLimit = 0

			# if colNum < colLimit:
			isAWall = maze[rowNum + 1][colNum] == 1
			if isAWall:
				#checks if this node has the ability to break
				#through a wall
				if saldo > 0:
					neighbors.append( Node(rowNum + 1, colNum, saldo - 1, maze) )
			else:
				# neighbors.append( Node(rowNum + 1, colNum, saldo, maze, maze[rowNum + 1]) )
				neighbors.append( Node(rowNum + 1, colNum, saldo, maze) )

		return neighbors

def answer(maze):
	g = Graph(maze, 1)
	return g.shortestDistanceToEnd()

print answer(maze)