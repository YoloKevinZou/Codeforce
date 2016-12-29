s = raw_input()

query_array = [0] * len(s)

for i in xrange(len(query_array)-1):
	query_array[i+1] = query_array[i] + (s[i] == s[i+1])

m = input()
for i in xrange(m):
	start,end = map(int, raw_input().split())
	end -=1
	print query_array[end] - query_array[start-1]