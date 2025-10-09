import sys

input = sys.stdin.readline
t = int(input().strip())
for _ in range(t):
    x, y, a, b = map(int, input().split())
    d = y - x
    s = a + b
    if d % s == 0:
        print(d // s)
    else:
        print(-1)
