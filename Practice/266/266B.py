n, t = map(int, raw_input().split())
inp = raw_input()

for i in xrange(t):
	inp = inp.replace('BG', 'GB')

print inp