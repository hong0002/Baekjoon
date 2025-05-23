def solve():
    k, n = map(int, input().split())
    # 최소: n번 먹고 한 번 빈 캔 선택
    minimum = n + 1
    # 최대: k*n번 먹고 한 번 빈 캔 선택
    maximum = k * n + 1
    print(minimum, maximum)

if __name__ == "__main__":
    solve()
