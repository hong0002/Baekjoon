def main():
    import sys
    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    logs = [int(input()) for _ in range(n-1)]
    S = set(logs)

    # 둘 다 등장 못 시키면 불가능
    if a not in S and b not in S:
        print(-1)
        return

    # 가능한 누락값 계산
    if a in S and b in S:
        # [a, b] 전부
        res = list(range(a, b+1))
    elif a in S:
        # b가 누락
        res = [b]
    else:
        # a가 누락
        res = [a]

    # 결과 출력
    print(*res)

if __name__ == "__main__":
    main()
