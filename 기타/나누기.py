def solve():
    import sys
    input = sys.stdin.readline

    N = int(input().rstrip())
    F = int(input().rstrip())

    base = (N // 100) * 100
    for i in range(100):
        if (base + i) % F == 0:
            # 두 자리로 맞추기 위해 zfill 사용
            print(str(i).zfill(2))
            return

if __name__ == "__main__":
    solve()
