s = raw_input()
subStr = "hello"
walker = 0

for i in s:
	if i == subStr[walker]:
		walker += 1
	if walker == len(subStr):
		break

print "YES" if walker == len(subStr) else "NO"