# 입력값을 받습니다.
X = int(input())
Y = int(input())
Z = int(input())

# 총 이동 시간 계산 (X + Y)
total_time = X + Y

# Z 시간 30분은 Z + 0.5 시간으로 변환
limit_time = Z + 0.5

# 총 이동 시간이 제한 시간 이내인지 판별하여 결과 출력
if total_time <= limit_time:
    print(1)
else:
    print(0)
