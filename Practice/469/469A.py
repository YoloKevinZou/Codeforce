n = input()
p = map(int, raw_input().split())
q = map(int, raw_input().split())

count = [False for _ in range(n+1)]

for i in range(1,len(p)):
	count[p[i]] = True

for i in range(1, len(q)):
	count[q[i]] = True

print "I become the guy." if sum(count[1:]) == n else "Oh, my keyboard!"