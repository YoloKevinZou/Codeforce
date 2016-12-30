a = input()
b = input()
c = input()

result = a+b*c

result = max(result, a*(b+c))
result = max(result, a*b*c)
result = max(result, (a+b)*c)
result = max(result, a+b+c)

print result