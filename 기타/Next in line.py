# 가장 어린 아이의 나이를 입력받음
youngest_age = int(input())

# 중간 아이의 나이를 입력받음
middle_age = int(input())

# 가장 나이 많은 아이의 나이를 계산
oldest_age = middle_age + (middle_age - youngest_age)

# 결과를 출력
print(oldest_age)
