# 입력 받기
age, alyssa_age, konari_age = map(int, input().split())

# 최대 가능한 a 값은 age // alyssa_age로 설정
found = False
for a in range(1, age // alyssa_age + 1):
    remainder = age - a * alyssa_age
    # remainder가 양수이면서 konari_age로 나누어떨어지는지 확인
    if remainder > 0 and remainder % konari_age == 0:
        k = remainder // konari_age
        if k > 0:  # k가 양의 정수인지 확인
            found = True
            break

# 결과 출력
print(1 if found else 0)
