def bfs(n,m):

	from collections import deque

	queue = deque()
	queue.append(n)
	result = 0
	visited = {}

	while queue:
		for _ in range(len(queue)):
			node = queue.popleft()
			visited[node] = True

			if node == 0:
				continue

			if node == m:
				return result

			if 2*node not in visited and 2*node < 2*m:
				queue.append(2*node)

			if node-1 not in visited:
				queue.append(node-1)

		result += 1

	return -1


n, m = map(int, raw_input().split())
print bfs(n,m)