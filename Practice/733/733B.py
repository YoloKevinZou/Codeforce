n = input()

left = []
right = []

for i in range(n):
	l, r = map(int, raw_input().split())
	left.append(l)
	right.append(r)

totalLeft = sum(left)
totalRight = sum(right)
maxBeauty = abs(totalLeft - totalRight)

col = 0

for i in range(n):
	flipL = totalLeft - left[i] + right[i]
	flipR = totalRight - right[i] + left[i]

	if abs(flipL - flipR) > maxBeauty:
		maxBeauty = abs(flipL - flipR)
		col = i + 1

print col