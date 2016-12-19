n = input()

a,b = 1, n

for i in xrange(1, n/2+1):
	if n % i == 0:
		if abs(n/i - i) < abs(b-a):
			a = i
			b = n/i
print(str(a) + " " + str(b))