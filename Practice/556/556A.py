n = raw_input()
digits = raw_input()
count = [0] * 2

for i in digits:
	count[int(i)] += 1

print len(digits) - (2*min(count))