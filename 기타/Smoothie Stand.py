import sys
input = sys.stdin.readline

def main():
    k, r = map(int, input().split())
    a = list(map(int, input().split()))  # 재고량 리스트, 길이 k

    max_revenue = 0

    for _ in range(r):
        *b, price = map(int, input().split())
        # b: 길이 k인 각 재료 소모량, price: 한 잔당 판매가

        # 이 레시피로 만들 수 있는 최대 스무디 개수 계산
        m = 10**18  # 충분히 큰 수로 초기화
        for ai, bi in zip(a, b):
            if bi > 0:
                m = min(m, ai // bi)

        # 매출 계산하여 최댓값 갱신
        revenue = m * price
        if revenue > max_revenue:
            max_revenue = revenue

    print(max_revenue)

if __name__ == "__main__":
    main()
