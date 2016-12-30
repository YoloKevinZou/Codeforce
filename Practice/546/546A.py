k,n,w = map(int, raw_input().split())
totalNeeded = ((w * (w+1))/2) * k
print 0 if n > totalNeeded else totalNeeded - n
