def calculate_total_cost(apples_per_bag, num_bags, cost_per_dozen):
    total_apples = apples_per_bag * num_bags  # 총 사과 개수
    dozens = (total_apples + 11) // 12  # 필요한 다스 수 계산
    total_cost = dozens * cost_per_dozen  # 총 가격 계산
    return total_cost

# 입력 처리
a, b = map(int, input().strip().split())
d = int(input().strip())

# 결과 계산 및 출력
print(calculate_total_cost(a, b, d))
