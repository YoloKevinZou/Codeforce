n, k = map(int, raw_input().split())

teams = map(int, raw_input().split())
teams.sort()

count = 0

for i in teams:
	if 5 - k >= i:
		count += 1

print count/3