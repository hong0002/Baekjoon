import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

overlap = max(0, min(b, d) - max(a, c))
ans = (b - a) + (d - c) - overlap

print(ans)
