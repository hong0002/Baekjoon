# 입력을 읽음
bills = list(map(int, input().split()))

# 각 briefcase의 지폐 종류
denominations = [1, 5, 10, 20, 50, 100]

# 각 briefcase의 총액 계산
total_money = [bills[i] * denominations[i] for i in range(6)]

# 최대 금액을 가지는 briefcase 찾기
max_money = max(total_money)

# 금액이 최대인 briefcase 중 가장 적은 지폐 개수를 가진 briefcase를 선택
min_bills = float('inf')
chosen_case = -1

for i in range(6):
    if total_money[i] == max_money:
        if bills[i] < min_bills:
            min_bills = bills[i]
            chosen_case = denominations[i]

# 결과 출력
print(chosen_case)
