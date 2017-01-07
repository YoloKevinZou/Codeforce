n = input()

numbers = map(int, raw_input().split())

result = 0
count = 1

numbers.append(float('-inf'))

for i in xrange(1,len(numbers)):
	if numbers[i] >= numbers[i-1]:
		count += 1
	else:
		result = max(result, count)
		count = 1

print result