import sys

def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out_lines = []

    for _ in range(t):
        n = int(data[idx]); k = int(data[idx+1])
        idx += 2

        if k != 1:
            out_lines.append(" ".join(map(str, range(1, n+1))))
        else:
            if n <= 3:
                out_lines.append("-1")
            else:
                seq = list(range(2, n+1, 2)) + list(range(1, n+1, 2))
                out_lines.append(" ".join(map(str, seq)))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
