import bisect

n = raw_input()
stores = map(int, raw_input().split())
q = input()

cost = [0 for _ in xrange(100001)] 
dp = [0 for _ in xrange(100001)] 

for i in stores:
	cost[i] += 1

for i in xrange(1, len(dp)):
	dp[i] = dp[i-1] + cost[i]

for i in xrange(q):
	coin = input()
	if coin > 100000:
		print dp[-1]
	else:
		print dp[coin]