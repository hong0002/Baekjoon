import math

n = int(input().strip())
q = math.isqrt(n)   # floor(sqrt(n))

if q * q < n:       # 만약 n보다 작으면 1 올려줌
    q += 1

print(q)
