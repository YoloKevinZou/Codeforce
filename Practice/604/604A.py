corrects = map(int, raw_input().split())
wrongs = map(int, raw_input().split())
hacks, failed = map(int, raw_input().split())
scores = [500,1000,1500,2000,2500]
result = 0

for i in xrange(5):
	result += max(0.3*scores[i], ((1-(corrects[i]/250.0))*scores[i]) - (50*wrongs[i]))

result += hacks * 100
result -= failed * 50

print int(result)