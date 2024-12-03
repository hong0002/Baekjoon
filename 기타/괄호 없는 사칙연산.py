def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        # 정수 나눗셈
        return a // b if a * b >= 0 else -(abs(a) // abs(b))

# 입력 받기
expression = input().split()
K1 = int(expression[0])
O1 = expression[1]
K2 = int(expression[2])
O2 = expression[3]
K3 = int(expression[4])

# 모든 괄호 조합 계산
result1 = calculate(calculate(K1, O1, K2), O2, K3)  # (K1 O1 K2) O2 K3
result2 = calculate(K1, O1, calculate(K2, O2, K3))  # K1 O1 (K2 O2 K3)

# 최소값과 최대값 출력
print(min(result1, result2))
print(max(result1, result2))
