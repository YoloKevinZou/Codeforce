import sys

n = input()
nums = map(int, raw_input().split())
sorted_nums = sorted(nums)

l = -1
r = -1

for i in range(1, len(nums)):
	if nums[i] < nums[i-1]:
		l = i-1
		r = i-1
		break

for j in range(r+1, len(nums)):
	if nums[j] > nums[j-1]:
		break
	r += 1

segment = nums[l:r+1]
rev_segment = segment[::-1]
x = nums[:l] + rev_segment + nums[r+1:]

if l == -1:
	print "yes"
	print 1, 1
elif x == sorted_nums:
	print "yes"
	print l+1, r+1
else:
	print "no"