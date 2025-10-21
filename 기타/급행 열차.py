import sys

def main():
    input = sys.stdin.readline
    N, M, K, X, Y = map(int, input().split())
    C = []
    for _ in range(N):
        A, B = map(int, input().split())
        C.append(X * A - Y * B)  # 가능 범위는 최대 약 1e12, 파이썬 int OK
    C.sort()
    ans = K * (X + Y) + sum(C[:M])
    print(ans)

if __name__ == "__main__":
    main()
