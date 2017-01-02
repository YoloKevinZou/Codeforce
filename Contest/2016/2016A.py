n, k = map(int, raw_input().split())

min_has = 240 - k

i = 1
result = 0

while i*5 <= min_has:
	result += 1
	min_has -= i*5
	i += 1

print result if result < n else n