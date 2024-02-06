# 각각의 크기에 해당하는 개수를 입력받음
S = int(input())  # small treats
M = int(input())  # medium treats
L = int(input())  # large treats

# 행복 점수 계산
happiness_score = 1 * S + 2 * M + 3 * L

# 행복 여부 판단
if happiness_score >= 10:
    print("happy")
else:
    print("sad")
