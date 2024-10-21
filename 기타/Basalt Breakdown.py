import math

# 입력 받기
A = int(input())

# 정육각형의 한 변의 길이를 구하는 공식
s = math.sqrt((2 * A) / (3 * math.sqrt(3)))

# 둘레 계산
P = 6 * s

# 결과 출력
print(f"{P:.8f}")
