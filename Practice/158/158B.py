import math

n = raw_input()

groups =map(int,raw_input().split())

count = [0] * 5

for i in groups:
	count[i] += 1

result = count[4]
result += count[3]
count[1] -= count[3]

result += count[2]/2
count[2] = count[2] % 2

if count[2] > 0:
	result += count[2]
	count[1] -= 2

import math
if count[1] > 0:
	result += int(math.ceil(count[1]/4.0))

print result