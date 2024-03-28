def calculate_commission(k):
    # 수수료 초기값 설정
    commission = 25 + k * 0.01
    # 최소 수수료인 100보다 작으면 100으로 설정
    if commission < 100:
        commission = 100
    # 최대 수수료인 2000보다 크면 2000으로 설정
    elif commission > 2000:
        commission = 2000
    return commission

# 입력 받기
k = int(input())

# 수수료 계산 후 출력
print("{:.2f}".format(calculate_commission(k)))
