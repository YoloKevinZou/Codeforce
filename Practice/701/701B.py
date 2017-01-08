n, m = map(int, raw_input().split())

appearedRow = {}
appearedCol = {}
total = n*n
totalRow = n
totalCol = n

for i in xrange(m):
	x, y = map(int, raw_input().split())
	if x not in appearedRow and y not in appearedCol:
		total -= (totalRow+totalCol-1)
		totalRow -= 1
		totalCol -= 1
	else:
		if x not in appearedRow:
			total -= (totalCol)
			if y not in appearedCol:
				totalCol -= 1
			totalRow -= 1
			
		if y not in appearedCol:
			total -= (totalRow)
			if x not in appearedRow:
				totalRow -= 1
			totalCol -= 1
	appearedRow[x] = True
	appearedCol[y] = True
	print total, 