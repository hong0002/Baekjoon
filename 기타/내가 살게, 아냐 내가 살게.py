import sys

def main():
    input = sys.stdin.readline

    N, M, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    # 각 사람의 누적 거리와 시도 횟수
    sum_len = [0] * N
    cnt = [0] * N

    # 열(라운드) 기준으로, 그 안에서 사람 1~N 순서
    for j in range(M):          # j: 0 ~ M-1 (j+1 번째 시도)
        for i in range(N):      # i: 0 ~ N-1 (사람 번호 i+1)
            sum_len[i] += A[i][j]
            cnt[i] += 1
            if sum_len[i] >= K:
                print(i + 1, cnt[i])
                return

if __name__ == "__main__":
    main()
