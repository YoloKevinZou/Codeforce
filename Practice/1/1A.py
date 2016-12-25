n,m,a=map(int,raw_input().split())

width = m/a if m%a == 0 else (m/a) + 1
height = n/a if n%a == 0 else (n/a) + 1

print(width * height)