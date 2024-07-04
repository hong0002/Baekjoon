def last_digit_of_factorial(n):
    # 팩토리얼 계산
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    # 마지막 자릿수 반환
    return factorial % 10

# 입력
T = int(input().strip())
test_cases = [int(input().strip()) for _ in range(T)]

# 각 테스트 케이스에 대해 결과 계산 및 출력
for n in test_cases:
    print(last_digit_of_factorial(n))
