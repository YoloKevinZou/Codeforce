n, t = map(int, raw_input().split())
books = map(int, raw_input().split())
books.append(float("-inf"))
frontPointer = 0
endPointer = 1
windowValue = books[0]
result = 0

while endPointer < len(books):
	
	if windowValue <= t:
		result = max(result, endPointer-frontPointer)
		windowValue += books[endPointer]
		endPointer += 1
	else:
		windowValue -= books[frontPointer]
		frontPointer += 1

print result