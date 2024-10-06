# 입력받기
buttons = list(map(int, input().split()))

# 자판기 음료 가격 설정
prices = {1: 500, 2: 800, 3: 1000}

# 총 금액 계산
total_cost = sum(prices[button] for button in buttons)

# 5000원에서 총 금액 빼기
change = 5000 - total_cost

# 거스름돈 출력
print(change)
