import sys

def solve():
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    t = int(next(it))
    out = []

    for tc in range(t):
        n = int(next(it))
        q = int(next(it))

        # 누적합
        pref = [0] * (n + 1)
        s = 0
        for k in range(n):
            s += int(next(it))
            pref[k + 1] = s

        for _ in range(q):
            i = int(next(it))
            j = int(next(it))
            if i > j:
                i, j = j, i
            out.append(str(pref[j + 1] - pref[i]))

        if tc != t - 1:
            out.append("")  # 테스트 케이스 사이 빈 줄

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
