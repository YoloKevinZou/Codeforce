n = raw_input()
flowers = map(int, raw_input().split())
high = max(flowers)
low = min(flowers)

if high == low:
	print 0, (flowers.count(high) * (flowers.count(high) - 1)) / 2
else:
	print high-low, flowers.count(high) * flowers.count(low)