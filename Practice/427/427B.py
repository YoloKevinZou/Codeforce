n,t,c = map(int, raw_input().split())

prisoners = map(int, raw_input().split())

frontPointer = 0
endPointer = 0
result = 0

while endPointer < n:

	if prisoners[endPointer] <= t:
		if endPointer - frontPointer +1 == c:
			result += 1
			frontPointer += 1
		endPointer += 1
	else:
		endPointer += 1
		frontPointer = endPointer

print result