def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    prev_a, prev_b = map(int, input().split())

    for _ in range(n - 1):
        a, b = map(int, input().split())
        # 한 팀이라도 점수가 줄어들면 시간 순서가 아님
        if a < prev_a or b < prev_b:
            print("no")
            return
        prev_a, prev_b = a, b

    print("yes")


if __name__ == "__main__":
    main()
