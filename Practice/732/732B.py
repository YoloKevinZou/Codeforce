n, k = map(int, raw_input().split())
walks = map(int, raw_input().split())
minWalk = 0

for i in range(1, len(walks)):
	totalWalk = walks[i] + walks[i-1]
	if totalWalk < k:
		minWalk += k - totalWalk
		walks[i] += k - totalWalk

print minWalk
print ' '.join(map(str,walks))