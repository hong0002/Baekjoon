# 입력 받기
H = int(input())
W = int(input())

# 직사각형의 짧은 변 찾기
shorter_side = min(H, W)

# 반지름 계산 (짧은 변의 절반) 및 센티미터 단위로 변환
radius_cm = (shorter_side / 2) * 100

# 정수로 출력
print(int(radius_cm))
