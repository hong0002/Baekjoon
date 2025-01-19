# 입력 처리
N, X, K = map(int, input().split())

# 공의 초기 위치
current_position = X

# K번의 교환을 처리
for _ in range(K):
    A, B = map(int, input().split())
    # 공이 A나 B에 있다면, 공은 교환된 다른 컵으로 이동
    if current_position == A:
        current_position = B
    elif current_position == B:
        current_position = A

# 최종 공의 위치 출력
print(current_position)
