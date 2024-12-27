# 입력 값 읽기
H, I, A, R, C = map(int, input().split())

# 첫 번째 항: H * I
first_term = H * I

# 두 번째 항: A * R * C
second_term = A * R * C

# 결과 계산: 첫 번째 항 - 두 번째 항
result = first_term - second_term

# 결과 출력
print(result)
