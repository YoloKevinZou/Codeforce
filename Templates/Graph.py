def getAdjacentFromList(adjList, origin):
	return adjList[origin]

# Check if Undirected graph has cycle
def dfs(adjList, vertex, visited, parent):

	if vertex in visited:
		return True

	visited[vertex] = True

	for i in getAdjacentFromList(adjList, vertex):
		if i == parent:
			continue
		value = dfs(adjList, i, visited, vertex)
		if value:
			return True

	return False