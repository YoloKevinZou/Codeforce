n = input()
s = list(raw_input())

outsideCount = 0
parentCount = 0
inParenthesis = False
s.append('_')

word = []

for i in range(len(s)):
	if s[i].isalpha():
		word.append(s[i])
	else:

		if not inParenthesis:
			outsideCount = max(outsideCount, len(word))
		else:
			parentCount += 1 if len(word) != 0 else 0

		word[:] = []

		if s[i] == '(':
			inParenthesis = True
		elif s[i] == ')':
			inParenthesis = False


print outsideCount, parentCount