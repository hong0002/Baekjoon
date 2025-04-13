def main():
    import sys
    input = sys.stdin.readline

    T = int(input().strip())
    for _ in range(T):
        x = int(input().strip())
        # 최소 게임 수는 2x - 1
        print(2 * x - 1)

if __name__ == '__main__':
    main()
