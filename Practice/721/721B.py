n, k = map(int, raw_input().split())

count = [0] * (101)

bestCase = 0
worstCase = 0

for i in range(n):
	pw = raw_input()
	count[len(pw)] += 1

dp = [0] * (101)

for i in range(1,len(dp)):
	dp[i] = count[i] + dp[i-1]

actualPw = raw_input()
actualPwLength = len(actualPw)

import math

bestCase = dp[actualPwLength-1] + int((math.floor(dp[actualPwLength-1]/k)*5)) + 1
worstCase = dp[actualPwLength] + int((math.floor(dp[actualPwLength]-1)/k)) * 5

print bestCase, worstCase