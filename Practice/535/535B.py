def isLucky(n):

	while n > 0:
		
		if n%10 != 4 and n%10 != 7:
			return False
		
		n/=10

	return True



n = input()

count = 0

i = 4
while True:

	if isLucky(i):
		count += 1

	if n == i:
		print count
		break
	i += 1