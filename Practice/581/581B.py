n = input()
houses = map(int, raw_input().split())

result = [0] * n
last = len(houses) - 2
maxHeight = houses[-1]

while last >= 0:
	if houses[last] <= maxHeight:
		result[last] = maxHeight - houses[last] + 1

	maxHeight = max(maxHeight, houses[last])
	last -= 1

print ' '.join(map(str, result))