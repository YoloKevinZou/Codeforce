n, boys = input(), map(int, raw_input().split())
m, girls = input(), map(int, raw_input().split())

result = 0

boyEnd = n-1
girlEnd = m-1

boys.sort()
girls.sort()

while boyEnd >= 0 and girlEnd >= 0:
	diff = abs(boys[boyEnd] - girls[girlEnd])

	if diff <= 1:
		result += 1
		boyEnd -= 1
		girlEnd -= 1
	elif boys[boyEnd] > girls[girlEnd]:
		boyEnd -= 1
	else:
		girlEnd -= 1

print result