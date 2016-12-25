inp = raw_input().lower()

vowels = "aeiouy"
result = []
for i in inp:
	if i not in vowels:
		result.append('.')
		result.append(i)

print(''.join(result))