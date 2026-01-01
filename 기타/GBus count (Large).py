import sys

def solve():
    data = sys.stdin.read().split()
    it = iter(data)

    T = int(next(it))
    out_lines = []

    MAXC = 5000

    for tc in range(1, T + 1):
        N = int(next(it))

        diff = [0] * (MAXC + 3)  # 여유 있게

        for _ in range(N):
            a = int(next(it))
            b = int(next(it))
            diff[a] += 1
            diff[b + 1] -= 1

        # 누적합으로 각 도시 커버 수 계산
        cover = [0] * (MAXC + 1)
        cur = 0
        for city in range(1, MAXC + 1):
            cur += diff[city]
            cover[city] = cur

        P = int(next(it))
        ans = []
        for _ in range(P):
            c = int(next(it))
            ans.append(str(cover[c]))

        out_lines.append(f"Case #{tc}: " + " ".join(ans))

    print("\n".join(out_lines))

if __name__ == "__main__":
    solve()
