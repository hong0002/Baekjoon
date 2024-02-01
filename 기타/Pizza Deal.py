import math

# 입력값 받기
A1, P1 = map(int, input().split())
R1, P2 = map(int, input().split())

# 한 조각 피자의 면적 계산
area_slice = A1

# 원 피자의 면적 계산
area_whole = math.pi * R1 ** 2

# 한 조각 피자의 가격 대비 면적
value_slice = area_slice / P1

# 원 피자의 가격 대비 면적
value_whole = area_whole / P2

# 더 가치 있는 것을 출력
if value_whole > value_slice:
    print('Whole pizza')
else:
    print('Slice of pizza')
