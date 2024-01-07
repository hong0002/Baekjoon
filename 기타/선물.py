def min_cost_for_socks(N, X, prices):
    min_cost = float('inf')

    for i in range(N - 1):
        cost = X * prices[i] + X * prices[i + 1]
        min_cost = min(min_cost, cost)

    return min_cost

# 입력 받기
N, X = map(int, input().split())
prices = list(map(int, input().split()))

# 최소 비용 계산 및 출력
result = min_cost_for_socks(N, X, prices)
print(result)

