import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    best = 0
    L = max(N, M)
    for i in range(L):
        curr = a[i] if i < N else 0
        past = b[i] if i < M else 0
        diff = past - curr
        if diff > best:
            best = diff

    print(best)

if __name__ == "__main__":
    main()
