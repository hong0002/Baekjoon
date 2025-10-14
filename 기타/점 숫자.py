import sys

def triangular(t):  # T_t = t*(t+1)//2
    return t*(t+1)//2

def num_to_xy(n):
    # find minimal k with T_k >= n
    # k는 대략 sqrt(2n) 수준이라 선형보다 이분 탐색이 편함
    lo, hi = 1, 200  # n < 10000이므로 k는 200 이하면 충분
    while lo < hi:
        mid = (lo + hi) // 2
        if triangular(mid) >= n:
            hi = mid
        else:
            lo = mid + 1
    k = lo
    x = n - triangular(k-1)
    y = k + 1 - x
    return x, y

def xy_to_num(x, y):
    return triangular(x + y - 2) + x

it = iter(sys.stdin.read().strip().split())
T = int(next(it))
out = []
for _ in range(T):
    a = int(next(it)); b = int(next(it))
    x1, y1 = num_to_xy(a)
    x2, y2 = num_to_xy(b)
    x, y = x1 + x2, y1 + y2
    out.append(str(xy_to_num(x, y)))

print("\n".join(out))
