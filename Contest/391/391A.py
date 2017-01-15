s = raw_input()

count = [0] * 256

for i in s:
	idx = ord(i)
	count[idx] += 1

result = float('inf')

result = min(result, count[ord('B')])
result = min(result, count[ord('u')]/2)
result = min(result, count[ord('l')])
result = min(result, count[ord('b')])
result = min(result, count[ord('a')]/2)
result = min(result, count[ord('s')])
result = min(result, count[ord('r')])

print result