import sys

data = sys.stdin.read().strip().split()
N, S = map(int, data[:2])
L = list(map(int, data[2:2+N]))

L.sort()
l, r = 0, N - 1
ans = 0

while l < r:
    if L[l] + L[r] <= S:
        ans += (r - l)  # L[l]은 l+1..r 모두와 가능
        l += 1
    else:
        r -= 1

print(ans)
