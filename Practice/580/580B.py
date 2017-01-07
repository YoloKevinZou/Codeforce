n, d = map(int, raw_input().split())

friends = []

for i in xrange(n):
	money, friendship = map(int, raw_input().split())
	friends.append((money,friendship))

friends.sort()

result = 0
frontPointer = 0
secondPointer = 0
tempMax = 0

while frontPointer < len(friends) and secondPointer < len(friends):

	diff = friends[secondPointer][0] - friends[frontPointer][0]

	if diff < d:
		tempMax += friends[secondPointer][1]
		secondPointer += 1
	else:
		tempMax -= friends[frontPointer][1]
		frontPointer += 1

	result = max(result, tempMax)

print result