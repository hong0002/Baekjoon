import math
import sys
input = sys.stdin.readline

N, W, H = map(int, input().split())
max_len = math.hypot(W, H)  # sqrt(W^2 + H^2)

for _ in range(N):
    L = int(input())
    if L <= max_len:
        print("YES")
    else:
        print("NO")
