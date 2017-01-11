n, x = map(int, raw_input().split())

chapters = map(int, raw_input().split())

chapters.sort()

result = 0
for i in chapters:
	result += x * i

	if x > 1:
		x -= 1


print result