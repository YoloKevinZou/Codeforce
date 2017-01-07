# Bottom Up DP
def bottomUp(nums):

	dp = [[float('-inf') for _ in range(n+1)] for _ in range(3)]

	for i in xrange(len(dp)):
		dp[i][0] = 0

	for i in xrange(len(nums)):
		for j in xrange(1, n+1):
			if j >= nums[i]:

				maxCopy = j/nums[i]
				result = float('-inf')

				while maxCopy > 0:
					take = dp[i-1][j-(nums[i]*maxCopy)] + maxCopy
					result = max(take, result)
					maxCopy -= 1

				dp[i][j] = max(result, dp[i-1][j])

	return dp[-1][-1]

# Better version of bottom up DP
def d(i, dp):
    return -1000000 if i < 0 else dp[i]

def bottomUp2(nums, n):
	a,b,c = nums[0],nums[1],nums[2]
	dp = [0]
	for i in xrange(1, n + 1):
		dp.append(1 + max(d(i - a, dp), d(i - b, dp), d(i - c, dp)))

	return dp[-1]


l = map(int,raw_input().split(' '))
n, nums = l[0], l[1:]

print bottomUp2(nums, n)