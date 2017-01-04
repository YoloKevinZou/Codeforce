n, m = map(int, raw_input().split())
nums = map(int, raw_input().split())

nums.sort()
result = float('inf')

for i in range(n-1, len(nums)):
	result = min(result, nums[i] - nums[i-(n-1)])

print result