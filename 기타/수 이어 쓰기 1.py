import sys

N = int(sys.stdin.readline().strip())

ans = 0
d = len(str(N))
p = 1  # 10^(k-1)

for k in range(1, d):
    ans += 9 * p * k
    p *= 10

ans += (N - p + 1) * d
print(ans)
