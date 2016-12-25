n,m,k=map(int,raw_input().split())

gNodes = map(int,raw_input().split())

gCached = {}

for i in gNodes:
	gCached[i] = True

print(gCached)

adjList = [[] for _ in range(n+1)]
# visited = [0 for _ in range(n+1)]

# notVisited = {}
# visiting = {}
visited = {}

for i in range(m):
	origin,destination = map(int,raw_input().split())
	adjList[origin].append(destination)
	adjList[destination].append(origin)
print(adjList)

def getAdjacentFromList(adjList, origin):
	return adjList[origin]

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

hasCycle = False
for i in range(1,n+1):
	print(visited)
	# if visited[i] == 0:
	if i not in visited:
		hasCycle = dfs(adjList, i, visited, None)
		if hasCycle:
			print(hasCycle)
			break
print(visited)
print(hasCycle)	

# check cycle
# def dfs(adjMatrix, visited, origin):

# 	if origin in visited:
# 		return True

# 	adjList = getAdj(adjMatrix, origin, visited)

# 	result = False
# 	for i in adjList:
# 		cycle = self.dfs(adjMatrix, visited, i)
# 		if cycle:
# 			result = True
# 	return result

# for i in range(n+1):
# 	print(getAdjacentFromList(adjList, i))
