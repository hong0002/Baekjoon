import sys
from math import gcd

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
N = next(it)
A = [next(it) for _ in range(N)]
X = next(it)

s = 0
cnt = 0
g = gcd  # 속도 미세 최적화
for v in A:
    if g(v, X) == 1:
        s += v
        cnt += 1

# 문제에서 최소 1개 이상 존재 보장
avg = s / cnt
# 절대/상대 오차 1e-6 허용 → 넉넉히 출력
print(f"{avg:.10f}".rstrip('0').rstrip('.') if '.' in f"{avg:.10f}" else f"{avg:.10f}")
