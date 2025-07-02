def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    for _ in range(N):
        A, B, X = map(int, input().split())
        W = A * (X - 1) + B
        print(W)

if __name__ == "__main__":
    main()
