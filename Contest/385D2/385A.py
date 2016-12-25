word = raw_input()
cached = {word:1}
count = 1


for i in range(1, len(word)):
	temp = word[i:] + word[:i]

	if temp not in cached:
		count += 1
	else:
		break

print(count)