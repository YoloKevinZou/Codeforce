n,m,k = map(int, raw_input().split())

armies = []
for i in xrange(m+1):
	armies.append(input())

fedor = armies[-1]
result = 0

for i in xrange(len(armies)-1):
	count = 0
	value = fedor ^ armies[i]

	for j in xrange(32):
		if value & (1 << j) != 0:
			count += 1

	if count <= k:
		result += 1

print result