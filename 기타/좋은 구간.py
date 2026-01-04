import sys
from bisect import bisect_left

input = sys.stdin.readline

L = int(input().strip())
S = list(map(int, input().split()))
n = int(input().strip())

S.sort()

# n이 집합 S에 있으면 좋은 구간 불가
if n in S:
    print(0)
    sys.exit()

idx = bisect_left(S, n)  # n이 들어갈 위치 (S[idx] > n 이 보장됨: n <= max(S) + n not in S)
l = S[idx - 1] if idx > 0 else 0
r = S[idx]

ans = (n - l) * (r - n) - 1
print(ans)
