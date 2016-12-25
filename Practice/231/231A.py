n = raw_input()

count = 0
for i in range(int(n)):
	votes = map(int, raw_input().split())

	if sum(votes) >= 2:
		count += 1

print(count)