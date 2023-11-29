# 참가자의 수 입력
N = int(input())

# 각 참가자의 점수 입력 및 최고 점수 초기화
max_score = 0
for _ in range(N):
    a, d, g = map(int, input().split())

    # 점수 계산
    score = a * (d + g) if a != (d + g) else a * 2 * (d + g)

    # 최고 점수 업데이트
    max_score = max(max_score, score)

# 최고 점수 출력
print(max_score)
