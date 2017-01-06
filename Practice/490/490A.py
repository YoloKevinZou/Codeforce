n = raw_input()

students = map(int, raw_input().split())

programming = []
math = []
PE = []

for index, value in enumerate(students):
	if value == 1:
		programming.append(index+1)
	elif value == 2:
		math.append(index+1)
	else:
		PE.append(index+1)

print min(len(programming), len(math), len(PE))

for i in range(min(len(programming), len(math), len(PE))):
	print programming[i], math[i], PE[i]