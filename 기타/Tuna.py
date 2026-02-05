import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    X = int(input().strip())

    total = 0
    for _ in range(N):
        p1, p2 = map(int, input().split())
        if abs(p1 - p2) <= X:
            total += max(p1, p2)
        else:
            p3 = int(input().strip())
            total += p3

    print(total)

if __name__ == "__main__":
    main()
