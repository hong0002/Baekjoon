import sys

def solve():
    data = list(map(int, sys.stdin.read().strip().split()))
    it = iter(data)
    T = next(it)
    out_lines = []
    for tc in range(1, T + 1):
        C = next(it)
        I = next(it)
        prices = [next(it) for _ in range(I)]
        seen = {}  # price -> index (1-based)
        a = b = -1
        for j, p in enumerate(prices, start=1):
            need = C - p
            if need in seen:
                a, b = seen[need], j
                if a > b:
                    a, b = b, a
                break
            if p not in seen:
                seen[p] = j
        out_lines.append(f"Case #{tc}: {a} {b}")
    print("\n".join(out_lines))

if __name__ == "__main__":
    solve()
