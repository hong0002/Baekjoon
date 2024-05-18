# 입력을 받아들입니다.
A, B, C = map(int, input().split())

# 1과 2의 개수를 셉니다.
count_1 = [A, B, C].count(1)
count_2 = [A, B, C].count(2)

# 더 많이 등장하는 숫자를 출력합니다.
if count_1 > count_2:
    print(1)
else:
    print(2)
