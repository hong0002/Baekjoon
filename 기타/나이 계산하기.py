def calculate_ages(birth_year, birth_month, birth_day, current_year, current_month, current_day):
    # 만 나이 계산
    if (current_month > birth_month) or (current_month == birth_month and current_day >= birth_day):
        man_age = current_year - birth_year
    else:
        man_age = current_year - birth_year - 1
    
    # 세는 나이 계산
    sae_age = current_year - birth_year + 1
    
    # 연 나이 계산
    yeon_age = current_year - birth_year
    
    return man_age, sae_age, yeon_age

# 입력을 받습니다.
birth_year, birth_month, birth_day = map(int, input().split())
current_year, current_month, current_day = map(int, input().split())

# 나이를 계산합니다.
man_age, sae_age, yeon_age = calculate_ages(birth_year, birth_month, birth_day, current_year, current_month, current_day)

# 결과를 출력합니다.
print(man_age)
print(sae_age)
print(yeon_age)
