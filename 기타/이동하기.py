import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())

    dp_prev = [0] * (M + 1)  # 이전 행 dp
    for _ in range(N):
        row = list(map(int, input().split()))
        dp_cur = [0] * (M + 1)  # 현재 행 dp
        for j in range(1, M + 1):
            val = row[j - 1]
            dp_cur[j] = max(dp_prev[j], dp_cur[j - 1], dp_prev[j - 1]) + val
        dp_prev = dp_cur

    print(dp_prev[M])

if __name__ == "__main__":
    main()
