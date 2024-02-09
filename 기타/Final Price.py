def calculate_final_price(n, initial_price, daily_changes):
    current_price = initial_price
    
    for change in daily_changes:
        current_price += change
    
    return current_price

# 입력 받기
n = int(input())
initial_price = int(input())
daily_changes = [int(input()) for _ in range(n - 1)]

# 최종 가격 계산
final_price = calculate_final_price(n, initial_price, daily_changes)

# 결과 출력
print(final_price)
