def calculate_min_payment(N, P):
    # 할인 쿠폰 조건 설정
    coupons = {
        5: lambda x: x - 500,
        10: lambda x: x * 0.9,
        15: lambda x: x - 2000,
        20: lambda x: x * 0.75
    }
    
    # 적용 가능한 모든 할인을 계산하여 최솟값을 찾음
    min_payment = P  # 기본적으로 할인이 없을 때의 금액
    for stamps, discount_func in coupons.items():
        if N >= stamps:
            discounted_price = discount_func(P)
            min_payment = min(min_payment, discounted_price)
    
    # 지불 금액이 음수가 될 수 없으므로 0과 비교하여 최솟값을 결정
    return max(0, int(min_payment))

# 입력 받기
N = int(input().strip())
P = int(input().strip())

# 결과 계산 및 출력
result = calculate_min_payment(N, P)
print(result)
