n = input()
people = map(int, raw_input().split())
people.sort()

waitTotal = 0
result = 0
for i in xrange(len(people)):
	if people[i] >= waitTotal:
		result += 1
		waitTotal += people[i]

print result