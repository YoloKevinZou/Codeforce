n,m = map(int, raw_input().split())
nums = map(int, raw_input().split())

dp = [0] * n

distinct_int = set()

for i in range(n-1, -1, -1):
	distinct_int.add(nums[i])
	dp[i] = len(distinct_int)

for i in range(m):
	print dp[input()-1]