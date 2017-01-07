s = raw_input()
t = raw_input()

distance = 0

for i in xrange(len(s)):
	if s[i] != t[i]:
		distance += 1

import sys
if distance % 2 != 0:
	print "impossible"
	sys.exit()

distance /= 2
result = []

for i in xrange(len(s)):
	if s[i] == t[i]:
		result.append(s[i])
	else:
		if distance > 0:
			result.append(s[i])
			distance -= 1
		else:
			result.append(t[i])

print ''.join(map(str,result))