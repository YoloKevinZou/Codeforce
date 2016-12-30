n = input()

# x = []
# y = []
# z = []

result = [0,0,0]

for i in xrange(n):
	forces = map(int, raw_input().split())

	for j in xrange(3):
		result[j] += forces[j]

print "YES" if result == [0,0,0] else "NO"