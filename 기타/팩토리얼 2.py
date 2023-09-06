def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 입력 받기
n = int(input())

# N의 팩토리얼 계산
result = factorial(n)

# 결과 출력
print(result)
