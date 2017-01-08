n, a = map(int, raw_input().split())
criminals = map(int, raw_input().split())
criminals = [-1] + criminals

maxDistance = 1
result = criminals[a]
leftPointer, rightPointer = a, a

while leftPointer > 0 or rightPointer <= n:

	leftPointer = a - maxDistance
	rightPointer = a + maxDistance

	leftValue = criminals[leftPointer] if leftPointer > 0 else 0
	rightValue = criminals[rightPointer] if rightPointer <= n else 0

	if leftPointer > 0 and rightPointer <= n:
		if criminals[leftPointer] == 1 and criminals[rightPointer] == 1:
			result += rightValue + leftValue

	elif leftPointer < 1:
		result += rightValue

	elif rightPointer > n:
		result += leftValue

	maxDistance += 1

print result