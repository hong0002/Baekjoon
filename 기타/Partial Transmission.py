import sys

def main():
    input = sys.stdin.readline

    n = int(input().strip())
    p = int(input().strip())
    arr = list(map(int, input().split()))  # n-1개

    total = n * (2 * p + (n - 1)) // 2   # p부터 p+n-1까지의 합
    missing = total - sum(arr)

    print(missing)

if __name__ == "__main__":
    main()
