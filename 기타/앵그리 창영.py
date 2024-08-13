import math

# 입력 받기
N, W, H = map(int, input().split())

# 박스의 대각선 길이 계산
diagonal = math.sqrt(W**2 + H**2)

# 각 성냥의 길이와 대각선 길이를 비교하여 결과 출력
for _ in range(N):
    match_length = int(input().strip())
    if match_length <= diagonal:
        print("DA")
    else:
        print("NE")
