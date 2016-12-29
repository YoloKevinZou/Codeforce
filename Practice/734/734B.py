k2, k3, k5, k6 = map(int, raw_input().split())

numberOf256 = min(k2,k5,k6)
numberOf32 = min(k2-numberOf256,k3)

print (numberOf256*256) + (numberOf32*32)