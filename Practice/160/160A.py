n = input()
nums = map(int, raw_input().split())

nums.sort()

total = sum(nums)
end = len(nums) - 1

take = 0
result = 0
while take <= total/2:
	take += nums[end]
	result += 1
	end -= 1

print result