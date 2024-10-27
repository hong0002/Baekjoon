# 입력
n = int(input().strip())
transactions = [int(input().strip()) for _ in range(n)]

# 초기화
current_balance = 0
min_balance = 0

# 각 거래 적용
for t in transactions:
    current_balance += t
    min_balance = min(min_balance, current_balance)

# 최소 시작 잔액 계산
initial_balance = abs(min_balance)

# 출력
print(initial_balance)
