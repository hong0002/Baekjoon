import sys

X, Y = map(int, sys.stdin.readline().split())
ans = X + Y + min(X // 10, Y // 10)
print(ans)
