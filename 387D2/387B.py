import sys

length = input()

code = raw_input()

if length%4 != 0:
	print("===")
	sys.exit()

# print(code)
average = length / 4
codeMap = { 'A':0, 'G':0, 'C':0, 'T':0, '?':0}

codeNeed = { 'A':0, 'G':0, 'C':0, 'T':0}

for i in code:
	codeMap[i] += 1
	if codeMap[i] > average and i != '?':
		print("===")
		sys.exit()

# print(codeMap)

for key, value in codeMap.iteritems():

	if value < average:
		codeNeed[key] = average - value



result = code

# print(codeNeed)

for key, value in codeNeed.iteritems():
	if value == 0:
		continue
	else:
		# print("HERE")
		for i in range(value):
			result = result.replace('?', key, 1)

		# i = value
		# while i >= 0:
			# result.replace('?', key, 1)
			# value -= 1
			# i -= 1

print(result)
# print(codeNeed)