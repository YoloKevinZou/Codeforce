n = input()

firstInp = map(int, raw_input().split())
secondInp = map(int, raw_input().split())
thirdInp = map(int, raw_input().split())

print(sum(firstInp) - sum(secondInp))
print(sum(secondInp) - sum(thirdInp))