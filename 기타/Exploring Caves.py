import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    try:
        T = int(next(it))
    except StopIteration:
        return

    out = []
    for _ in range(T):
        x = y = 0
        best_x = 0
        best_y = 0
        best_r2 = 0  # (0,0)도 후보에 포함

        while True:
            dx = int(next(it)); dy = int(next(it))
            if dx == 0 and dy == 0:
                # 동굴 종료
                out.append(f"{best_x} {best_y}")
                break
            x += dx
            y += dy
            r2 = x*x + y*y
            if r2 > best_r2 or (r2 == best_r2 and x > best_x):
                best_r2 = r2
                best_x, best_y = x, y

    print("\n".join(out))

if __name__ == "__main__":
    solve()
