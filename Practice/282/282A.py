n = input()

count = 0
for i in range(n):
	op = raw_input()
	if "++" in op:
		count += 1
	else:
		count -= 1
print count