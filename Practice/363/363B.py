n, k = map(int, raw_input().split())
fences = map(int, raw_input().split())

index = 0
dp = [0] * (n+1)

for i in range(1, n+1):
	dp[i] = fences[i-1] + dp[i-1]

minimum_height = float('inf')
for i in range(k, n+1):
	total = dp[i] - dp[i-k]
	if total < minimum_height:
		minimum_height = total
		index = i - k + 1

print index