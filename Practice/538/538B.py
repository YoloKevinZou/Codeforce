def isQuasi(n):

	nList = str(n)

	for i in nList:
		if (i != '0' and i != '1'):
			return False

	return True


def dp(n, quasi, i, memo):

	if n in memo:
		return memo[n]

	if n == quasi[i]:
		return [quasi[i]]

	if n < 10 or i <= 0:
		return [1]*n
	print n
	
	numberOfCopy = (n/quasi[i])
	result = []
	maxLength = float('inf')
 	while numberOfCopy * quasi[i] >= 0:
 		temp = [quasi[i]] * numberOfCopy 
		temp += dp(n-(numberOfCopy*quasi[i]), quasi, i-1,memo)
		if len(temp) < maxLength:
			result = temp[:]
			# print result
			maxLength = len(temp)
		numberOfCopy -= 1

	memo[n] = result

	return result


n = input()

quasi = []

for i in range(1, 1000001):
	if isQuasi(i):
		quasi.append(i)


memo = {}
result = dp(n, quasi, len(quasi)-1, memo)
print len(result)
print ' '.join(map(str, result))
# print quasi
# for i in range(len(quasi)-1,-1,-1):
	# if n >= quasi[i]:
		# amountOfTime = (n/quasi[i])
		# for j in range(amountOfTime):
			# result.append(str(quasi[i]))

		# n -= (amountOfTime * quasi[i])

# print len(result)
# print ' '.join(result[::-1])
