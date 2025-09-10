import sys

it = iter(sys.stdin.read().strip().split())
T = int(next(it))
out = []
for _ in range(T):
    V = int(next(it)); E = int(next(it))
    out.append(str(E - V + 2))
print("\n".join(out))
