import sys

data = list(map(int, sys.stdin.read().split()))
it = iter(data)
N = next(it); M = next(it)

deg = [0]*(N+1)
for _ in range(M):
    a = next(it); b = next(it)
    deg[a] += 1
    deg[b] += 1

print("\n".join(str(deg[i]) for i in range(1, N+1)))
