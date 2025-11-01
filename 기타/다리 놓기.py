import sys
from math import gcd

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().split())
    # C(M, N) = C(M, M-N) 이므로 더 작은 쪽으로 계산
    k = min(N, M - N)
    numer = 1
    denom = 1
    for i in range(1, k + 1):
        numer *= (M - k + i)   # M-k+1, ..., M
        denom *= i             # 1, ..., k
        g = gcd(numer, denom)
        numer //= g
        denom //= g
    print(numer)  # denom은 항상 1이 됨
