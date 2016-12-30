n = input()

result = 0

for i in xrange(n+1):
	result += len(str(i))

print result