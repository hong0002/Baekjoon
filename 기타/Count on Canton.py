import sys, math

def nth_term(n: int):
    # 가장 작은 k: T_k >= n
    s = math.isqrt(1 + 8*n)
    k = (s - 1) // 2
    if k * (k + 1) // 2 < n:
        k += 1

    prev = k * (k - 1) // 2        # T_{k-1}
    d = n - prev                   # 1-based index within diagonal

    if k % 2 == 1:                 # odd diagonal
        num = k - d + 1
        den = d
    else:                          # even diagonal
        num = d
        den = k - d + 1
    return num, den

out = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    p, q = nth_term(n)
    out.append(f"TERM {n} IS {p}/{q}")

sys.stdout.write("\n".join(out))
