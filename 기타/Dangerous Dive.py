import sys

data = sys.stdin.read().strip().split()
N, R = map(int, data[:2])
returned = set(map(int, data[2:]))

missing = [str(i) for i in range(1, N+1) if i not in returned]

if missing:
    print(" ".join(missing) + " ")
else:
    print("*")
