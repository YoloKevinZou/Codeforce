n = input()

total_cost = 0
min_cost = float('inf')

for i in range(n):
	needed, cost = map(int, raw_input().split())
	total_cost += min(min_cost * (i+1), cost * (i+1))
	min_cost = min(min_cost, cost)

print total_cost