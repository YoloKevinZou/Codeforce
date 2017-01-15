n = input()
nums = map(int, raw_input().split())

count = [0] * 100001

for i in nums:
	count[i] += 1

result = 1
for i in xrange(2,  100001):

	tempCount = 0
	multiplier = 1

	while i*multiplier < 100001:
		tempCount += count[i*multiplier]
		multiplier += 1

	result = max(result, tempCount)

print result
