n = input()
letters = map(int, raw_input().split())

import sys
if sum(letters) == 0:
	print 0
	sys.exit()

startIndex = 0

for i in xrange(n):
	if letters[i] == 1:
		startIndex = i
		break

result = letters[startIndex]

for i in xrange(startIndex+1, n):
	if letters[i] == 1:
		if letters[i] == letters[i-1]:
			result += 1
		else:
			result += 2

print result