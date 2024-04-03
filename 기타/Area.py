# 입력 받기
n = int(input())

# 가장 큰 면적 초기값 설정
max_area = 0

# 각각의 프레임에 대해 최대 면적 계산
for _ in range(n):
    h, w = map(int, input().split())
    area = h * w
    # 현재 프레임의 면적이 최대면적보다 크면 갱신
    if area > max_area:
        max_area = area

# 최대 면적 출력
print(max_area)
