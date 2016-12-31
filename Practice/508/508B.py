n = raw_input()

nList = list(n)
lastDigit = int(nList[-1])
evenIndex = -1

for i in range(len(nList)):
	if int(nList[i]) % 2 == 0 and int(nList[i]) < lastDigit:
		evenIndex = i
		break

if evenIndex == -1:
	for i in range(len(nList)-1, -1, -1):
		if int(nList[i]) > lastDigit and int(nList[i]) % 2 == 0:
			evenIndex = i
			break

if evenIndex == -1:
	print -1
else:
	nList[evenIndex], nList[-1] = nList[-1], nList[evenIndex]
	print ''.join(nList)