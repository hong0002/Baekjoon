import sys

input = sys.stdin.readline

N = int(input().strip())
nums = [list(map(int, input().split())) for _ in range(N)]

scores = [0] * N

# 3번의 게임(열) 각각 처리
for c in range(3):
    cnt = [0] * 101  # 숫자 범위가 1..100
    for i in range(N):
        cnt[nums[i][c]] += 1
    for i in range(N):
        v = nums[i][c]
        if cnt[v] == 1:
            scores[i] += v

print("\n".join(map(str, scores)))
