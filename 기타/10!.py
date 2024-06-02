# 입력 받기
N = int(input())

# N! 계산
factorial = 1
for i in range(1, N + 1):
    factorial *= i

# N!초가 몇 주와 동일한지 계산
weeks = factorial // (7 * 24 * 60 * 60)

# 결과 출력
print(weeks)

