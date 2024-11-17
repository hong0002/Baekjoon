while True:
    # 첫 줄 입력: 사탕 개수 n
    n = int(input())
    if n == 0:  # 입력 종료 조건
        break

    # 두 번째 줄 입력: 각 사탕의 가격 리스트
    prices = list(map(int, input().split()))

    total_spent = 0  # 총 소비 금액

    # 사탕 가격 리스트 순회
    for price in prices:
        if total_spent + price <= 300:
            total_spent += price

    # 결과 출력
    print(total_spent)
