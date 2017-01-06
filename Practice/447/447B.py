s = raw_input()
k = input()

w = map(int, raw_input().split())

count = [0] * 26

for i in range(len(w)):
	count[i] = w[i]

total = 0

for index, value in enumerate (s):
	idx = ord(value) - ord('a')
	total += (count[idx] * (index+1))

highest = max(count)

for j in xrange(len(s)+1, len(s) + k + 1):
	total += (highest * j)

print total
