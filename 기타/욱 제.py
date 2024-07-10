import math

# 입력을 받습니다.
A, B = map(int, input().split())

# M을 계산합니다.
M = (B - A) / 400

# 욱이 제를 이길 확률을 계산합니다.
P = 1 / (1 + 10**M)

# 결과를 출력합니다.
print(f"{P:.16f}")
