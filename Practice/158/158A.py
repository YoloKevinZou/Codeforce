import sys

n,k=map(int,raw_input().split())

scores = map(int,raw_input().split())

kScore = scores[k-1]

count = 0
for i in range(len(scores)):
	if scores[i] >= kScore and scores[i] != 0:
		count += 1
	else:
		break

print(count)