import sys

ds, ys = map(int, sys.stdin.readline().split())
dm, ym = map(int, sys.stdin.readline().split())

for t in range(1, 5001):
    if (t + ds) % ys == 0 and (t + dm) % ym == 0:
        print(t)
        break
