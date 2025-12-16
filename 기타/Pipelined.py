import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    s = list(map(int, input().split()))
    print(max(s) + (N - 1))

if __name__ == "__main__":
    main()
