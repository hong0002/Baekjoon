import math

def solve_quadratic(A, B):
    # 이차방정식 x^2 + 2Ax + B = 0의 해 구하기
    discriminant = 4 * A * A - 4 * B  # 판별식 Δ = 4A^2 - 4B
    
    # 근이 두 개인 경우
    if discriminant > 0:
        sqrt_disc = math.isqrt(discriminant)  # sqrt(Δ) 값
        x1 = (-2 * A + sqrt_disc) // 2
        x2 = (-2 * A - sqrt_disc) // 2
        return sorted([x1, x2])  # 오름차순으로 반환
    # 근이 중근인 경우
    elif discriminant == 0:
        x = -2 * A // 2  # 중근 계산
        return [x]
    else:
        return []  # 이 문제에서는 판별식이 음수일 경우는 없다고 가정

# 입력 받기
A, B = map(int, input().split())

# 결과 출력
result = solve_quadratic(A, B)
print(" ".join(map(str, result)))
