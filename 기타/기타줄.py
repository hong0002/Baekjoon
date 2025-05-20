import math

def min_cost(N, prices):
    # prices: [(package_price, single_price), ...]
    p_min = min(p for p, s in prices)
    s_min = min(s for p, s in prices)

    # 1) 전부 패키지
    cost1 = math.ceil(N / 6) * p_min
    # 2) 몫만큼 패키지 + 나머지는 낱개
    cost2 = (N // 6) * p_min + (N % 6) * s_min
    # 3) 전부 낱개
    cost3 = N * s_min

    return min(cost1, cost2, cost3)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    prices = [tuple(map(int, input().split())) for _ in range(M)]
    print(min_cost(N, prices))
