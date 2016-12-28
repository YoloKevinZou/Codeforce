n, l = map(int, raw_input().split())
latterns = map(int, raw_input().split())
latterns.sort()

maxGap = max(float(latterns[0]), l - float(latterns[-1]))

for i in range(1, len(latterns)):
	maxGap = max(maxGap, (latterns[i] - latterns[i-1])/2.0)
	
print maxGap