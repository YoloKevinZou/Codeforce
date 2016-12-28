n = raw_input()
numberOfWorms = map(int, raw_input().split())
m = input()
juicyWorms = map(int, raw_input().split())

for i in range(1,len(numberOfWorms)):
	numberOfWorms[i] += numberOfWorms[i-1]

for i in juicyWorms:

	start = 0
	end = len(numberOfWorms) - 1

	while start <= end:
		mid = (end - start) / 2 + start

		if numberOfWorms[mid] < i:
			start = mid + 1
		else:
			end = mid - 1
	print start + 1