n = input()
computers = map(int, raw_input().split())

direction = 1
numberOfInfo = 0
start = 0
result = 0

while numberOfInfo < n:

	if start == -1:
		direction = 1
		result += 1
		start += direction
		continue
	elif start == n:
		direction = -1
		result += 1
		start += direction
		continue

	if computers[start] <= numberOfInfo and computers[start] != -1:
		numberOfInfo += 1
		computers[start] = -1

	start += direction

print result