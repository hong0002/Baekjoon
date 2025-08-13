def digit_sum(n: int) -> int:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

L = int(input().strip())
D = int(input().strip())
X = int(input().strip())

# 최소 N
N = None
for n in range(L, D + 1):
    if digit_sum(n) == X:
        N = n
        break

# 최대 M
M = None
for m in range(D, L - 1, -1):
    if digit_sum(m) == X:
        M = m
        break

print(N)
print(M)
