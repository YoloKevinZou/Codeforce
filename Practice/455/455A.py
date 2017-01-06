n = input()

nums = map(int, raw_input().split())

count = [0] * 100001

for i in nums:
	count[i] += 1

dp = [0] * 100001
dp[1] = count[1]
for i in range(2, len(dp)):
	dp[i] = max(dp[i-1],dp[i-2] + count[i]*i)

print dp[-1]