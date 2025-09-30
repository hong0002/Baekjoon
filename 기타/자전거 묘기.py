import sys

input = sys.stdin.readline

N = int(input().strip())
h = list(map(int, input().split()))
# 1-indexed로 맞추기
h = [0] + h

dp = [0] * (N + 2)  # dp[N+1]은 더미
for i in range(N, 0, -1):
    nxt = i + h[i] + 1
    if nxt > N:
        dp[i] = 1
    else:
        dp[i] = 1 + dp[nxt]

print(*dp[1:N+1])
