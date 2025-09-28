import sys

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split()))  # 1-index

    # dp[t][i] = t초 후 위치 i에서의 최대 크기 (불가능은 -1)
    dp = [[-1]*(N+1) for _ in range(M+1)]
    dp[0][0] = 1

    for t in range(M):
        for i in range(N+1):
            if dp[t][i] < 0:
                continue
            # 이미 끝에 도달했다면 유지만 가능
            if i == N:
                if dp[t+1][N] < dp[t][N]:
                    dp[t+1][N] = dp[t][N]
                continue

            # 1) 굴리기: +1칸
            if i + 1 <= N:
                val = dp[t][i] + arr[i+1]
                if dp[t+1][i+1] < val:
                    dp[t+1][i+1] = val

            # 2) 던지기: +2칸
            if i + 2 <= N:
                val = (dp[t][i] // 2) + arr[i+2]
                if dp[t+1][i+2] < val:
                    dp[t+1][i+2] = val

    print(max(dp[M]))

if __name__ == "__main__":
    solve()
