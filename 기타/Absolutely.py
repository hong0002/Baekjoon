import math

# 데이터셋의 개수를 입력 받음
n = int(input())

# n번의 데이터셋에 대해 반복
for _ in range(n):
    # 두 값 입력 받음
    a, b = map(float, input().split())
    
    # 두 값의 절대 거리 계산
    distance = abs(a - b)
    
    # 소수점 한 자리까지 반올림하여 출력
    print(round(distance, 1))
