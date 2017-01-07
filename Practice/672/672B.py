n = input()
s = raw_input()
import sys
if n > 26:
	print -1
	sys.exit()


count = [0] * 26

for i in s:
	idx = ord(i) - ord('a')
	count[idx] += 1

numberOfUnique = 0

for i in count:
	if i > 0:
		numberOfUnique += 1

print n-numberOfUnique