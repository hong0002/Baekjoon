import math

# 입력 받기
a, b, c = map(int, input().split())

# 빈칸 계산
if a == 0:
    result = c ** 2 - b
elif b == 0:
    result = c ** 2 - a
elif c == 0:
    result = int(math.sqrt(a + b))

# 결과 출력
print(result)
