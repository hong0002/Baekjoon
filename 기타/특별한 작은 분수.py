def calculate_fraction_height(x0, N):
    current_height = x0

    for _ in range(N):
        if current_height % 2 == 0:
            current_height = current_height // 2 ^ 6
        else:
            current_height = (2 * current_height) ^ 6

    return current_height

# 입력 받기
x0, N = map(int, input().split())

# N초에서의 분수의 높이 계산하고 출력
result = calculate_fraction_height(x0, N)
print(result)
