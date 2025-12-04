import sys

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    total_profit = 0

    for _ in range(N):
        A, B, C = map(int, input().split())
        # 그날 최선의 선택: 세 회사 중 최대 이익과 0 중 최댓값
        total_profit += max(0, A, B, C)

    print(total_profit)
