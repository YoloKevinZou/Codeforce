n = input()

tempTotal = 0
curD = 0
result = 0
for i in range(n):
	rate, division = map(int, raw_input().split())

	if curD == 0:
		curD = division

	if curD == division:
		tempTotal += rate

	if curD == 2 and division == 1:
		if result == 0:
			result = 1899 + tempTotal
		tempTotal = rate

	if curD == 1 and division == 2:
		if result == 0:
			

	# if curD != division:
		# tempTotal = 0 
