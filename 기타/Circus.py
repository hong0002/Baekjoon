import math

# 입력 받기
area = int(input())

# 반지름 계산
radius = math.sqrt(area / math.pi)

# 둘레 계산
circumference = 2 * math.pi * radius

# 결과 출력
print(circumference)
