B = int(input())

# 대기압 계산
P = 5 * B - 400

# 레벨 판별
if P < 100:
    level = 1  # 위에 있는 경우
elif P == 100:
    level = 0  # 해수면에 있는 경우
else:
    level = -1  # 아래에 있는 경우

# 결과 출력
print(P)
print(level)
