# 사무용품과 그 비용을 사전으로 정의
item_costs = {
    "Paper": 57.99,
    "Printer": 120.50,
    "Planners": 31.25,
    "Binders": 22.50,
    "Calendar": 10.95,
    "Notebooks": 11.20,
    "Ink": 66.95
}

total_cost = 0.0

# 입력 처리
while True:
    item = input().strip()
    if item == "EOI":
        break
    if item in item_costs:
        total_cost += item_costs[item]

# 결과 출력
print(f"${total_cost:.2f}")
