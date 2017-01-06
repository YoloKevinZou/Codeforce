# Row Check

def rowCheck(i,j,matrix):

	count = 0
	originalValue = matrix[i][j]
	matrix[i][j] = 'x'

	tempJ = j

	while tempJ >= 0:
		if matrix[i][tempJ] == 'x':
			count += 1
			tempJ -= 1
		else:
			break

	tempJ = j+1

	while tempJ < 4:
		if matrix[i][tempJ] == 'x':
			count += 1
			tempJ += 1
		else:
			break


	# for tempJ in range(4):
	# 	if matrix[i][tempJ] == 'x':
	# 		count += 1
	# 	else:
	# 		break

	matrix[i][j] = originalValue
	# print "ROW COUNT:", count
	return True if count >= 3 else False

def columnCheck(i, j, matrix):

	count = 0
	originalValue = matrix[i][j]
	matrix[i][j] = 'x'
	# print matrix[i][j]
	tempI = i

	while tempI >= 0:

		if matrix[tempI][j] == 'x':

			count += 1
			tempI -= 1
		else:
			break

	tempI = i+1

	while tempI < 4:
		if matrix[tempI][j] == 'x':
			count += 1
			tempI += 1
		else:
			break

	
	# for tempI in range(4):
		# if matrix[j][tempI] == 'x':
			# count += 1
		# else:
			# break
	# print i,j 
	# print "COL: ", count
	# print matrix
	matrix[i][j] = originalValue

	return True if count >= 3 else False


def leftDiagCheck(i,j, matrix):

	originalValue = matrix[i][j]
	matrix[i][j] = 'x'

	tempI = i
	tempJ = j
	count = 0
	while tempI >= 0 and tempJ >= 0:
		if matrix[tempI][tempJ] == 'x':
			count += 1
			tempI -= 1
			tempJ -= 1
		else:
			break

	tempI = i+1
	tempJ = j+1

	while tempJ < 4 and tempI < 4:
		if matrix[tempI][tempJ] == 'x':
			count += 1
			tempI += 1
			tempJ += 1
		else:
			break

	matrix[i][j] = originalValue
	# print i,j
	# print "LEFT DIAG: ", count
	return True if count >= 3 else False


def rightDiagCheck(i,j,matrix):

	originalValue = matrix[i][j]
	matrix[i][j] = 'x'

	count = 0

	tempI = i
	tempJ = j

	while tempI >= 0 and tempJ < 4:
		if matrix[tempI][tempJ] == 'x':
			count += 1
			tempI -= 1
			tempJ += 1
		else:
			break

	tempI = i+1
	tempJ = j-1

	while tempI < 4 and tempJ >= 0:
		if matrix[tempI][tempJ] == 'x':
			count += 1
			tempI += 1
			tempJ -= 1
		else:
			break

	matrix[i][j] = originalValue
	# print "RIGHT DIAG: ", count
	return True if count >= 3 else False

n = 4

matrix = []

for i in range(n):
	matrix.append(map(str,raw_input()))
import sys
for i in range(4):
	for j in range(4):
		if matrix[i][j] == '.':
			if rowCheck(i,j,matrix) or columnCheck(i,j,matrix) or leftDiagCheck(i,j,matrix) or rightDiagCheck(i,j,matrix):
				print "YES"
				sys.exit()

print "NO"