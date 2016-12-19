n,m=map(int,raw_input().split())

matrix = [[] for _ in range(n)]

for i in range(n):
	line = raw_input()

	for char in line:
		matrix[i].append(char)

	for char in line:
		matrix[i].append(char)		

def solve(matrix):
	count = 0
	for i in range(len(matrix)):
		numberOfX = 0
		for j in range(len(matrix[i])):
			if matrix[i][j] == 'X':
				numberOfX += 1

		if numberOfX != 0 and count == 0:
			count = numberOfX
		elif numberOfX != 0 and count != 0 and numberOfX != count:
			print("NO")
			return

	print("YES")

solve(matrix)