multiples = [input() for _ in range(4)]
d = input()
hit = 0
for i in range(1, d+1):
	for j in multiples:
		if i % j == 0:
			hit += 1
			break
print hit