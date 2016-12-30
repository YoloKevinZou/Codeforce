n = raw_input()
soldiers = map(int, raw_input().split())

soldiers.sort()

result = 0

for i in xrange(1, len(soldiers)):
	if soldiers[i] == soldiers[i-1]:
		soldiers[i] += 1
		result += 1
	elif soldiers[i] < soldiers[i-1]:
		result += (soldiers[i-1] - soldiers[i]) + 1
		soldiers[i] += (soldiers[i-1] - soldiers[i]) + 1
		
print result