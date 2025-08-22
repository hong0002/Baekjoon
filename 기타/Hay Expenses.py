import sys

data = list(map(int, sys.stdin.read().split()))
N, Q = data[0], data[1]

H = data[2:2+N]
idx = 2 + N

# 누적 합 (1-indexed를 맞추기 위해 앞에 0을 둠)
P = [0]
for x in H:
    P.append(P[-1] + x)

out = []
for _ in range(Q):
    S, E = data[idx], data[idx+1]
    idx += 2
    out.append(str(P[E] - P[S-1]))

print("\n".join(out))
