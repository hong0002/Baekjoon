def solve():
    T = int(input().strip())
    # 10초 단위로만 맞출 수 있으니
    if T % 10 != 0:
        print(-1)
        return

    a = T // 300
    T %= 300
    b = T // 60
    T %= 60
    c = T // 10

    print(a, b, c)

if __name__ == "__main__":
    solve()
