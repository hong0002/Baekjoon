import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    A = list(map(int, input().split()))

    # prefix sums
    P = [0] * (N + 1)   # sum
    Q = [0] * (N + 1)   # sum of squares
    for i, x in enumerate(A, start=1):
        P[i] = P[i - 1] + x
        Q[i] = Q[i - 1] + x * x

    out_lines = []
    for k in range(1, N + 1):
        best_i = 1
        best_val = -1  # k*sum_sq - sum^2 (always >= 0)

        for start in range(0, N - k + 1):  # 0-based start
            s = P[start + k] - P[start]
            sq = Q[start + k] - Q[start]
            val = k * sq - s * s

            if val > best_val:
                best_val = val
                best_i = start + 1  # to 1-based

        out_lines.append(str(best_i))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
