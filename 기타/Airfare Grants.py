# 입력 받기
N = int(input())
prices = [int(input()) for _ in range(N)]

# 보고용 항공권과 실제 구매 항공권 가격 결정
max_price = max(prices)
min_price = min(prices)

# 지원 한도 계산
reimbursement_limit = max_price // 2

# 최종 비용 계산
net_cost = min_price - min(min_price, reimbursement_limit)

# 결과 출력
print(net_cost)
