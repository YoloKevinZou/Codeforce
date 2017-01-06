n = input()

nums = map(int, raw_input().split())

result = 0
count = 1

nums.append(float('-inf'))

for i in xrange(1, len(nums)):
	if nums[i] > nums[i-1]:
		count += 1
	else:
		result = max(count, result)
		count = 1

print result