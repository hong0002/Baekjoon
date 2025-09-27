import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    T = int(next(it))
    out_lines = []
    for tc in range(1, T + 1):
        N = int(next(it))
        V = [int(next(it)) for _ in range(N)]
        best = -1
        ans = 0
        for i in range(N):
            left_ok = V[i] > best
            right_ok = (i == N - 1) or (V[i] > V[i + 1])
            if left_ok and right_ok:
                ans += 1
            if V[i] > best:
                best = V[i]
        out_lines.append(f"Case #{tc}: {ans}")
    print("\n".join(out_lines))

if __name__ == "__main__":
    solve()
