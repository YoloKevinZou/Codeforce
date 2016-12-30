n = input()
pylons = map(int, raw_input().split())

cost = pylons[0]
energy = 0
for i in range(n-1):
	if pylons[i]+energy >= pylons[i+1]:
		energy -= pylons[i+1] - pylons[i]
	else:
		cost += pylons[i+1] - (pylons[i] + energy)
		energy = 0

print cost