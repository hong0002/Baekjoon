def calculate_tickets(n, A, purchases):
    total_tickets = 0
    for purchase in purchases:
        tickets = purchase // A
        total_tickets += tickets
    return total_tickets

# 입력 처리
n, A = map(int, input().split())
purchases = list(map(int, input().split()))

# 함수 호출 및 결과 출력
print(calculate_tickets(n, A, purchases))
