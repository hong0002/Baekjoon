def find_equation(A, B, C):
    if A + B == C:
        print(f"{A}+{B}={C}")
    elif A - B == C:
        print(f"{A}-{B}={C}")
    elif A * B == C:
        print(f"{A}*{B}={C}")
    elif B != 0 and A / B == C:
        print(f"{A}/{B}={C}")
    elif A == B + C:
        print(f"{A}={B}+{C}")
    elif A == B - C:
        print(f"{A}={B}-{C}")
    elif A == B * C:
        print(f"{A}={B}*{C}")
    elif C != 0 and A == B / C:
        print(f"{A}={B}/{C}")

# 입력 받기
A, B, C = map(int, input().split())

# 결과 출력
find_equation(A, B, C)
