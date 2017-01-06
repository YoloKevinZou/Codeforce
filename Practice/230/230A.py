s, n = map(int, raw_input().split())

dragons  = []

for i in range(n):
	strength, bonus = map(int, raw_input().split())
	dragons.append((strength, bonus))

dragons.sort()

won = True

for d in dragons:
	if s > d[0]:
		s += d[1]
	else:
		won = False
		break

print "YES" if won else "NO"