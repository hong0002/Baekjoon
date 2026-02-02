import sys
from collections import Counter

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    rows = [input().strip() for _ in range(n)]  # 각 줄은 길이 m
    cnt = Counter(rows)
    print(max(cnt.values()))

if __name__ == "__main__":
    main()
