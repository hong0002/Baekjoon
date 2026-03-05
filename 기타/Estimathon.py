import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    if n < m:
        print("NE")
        return

    tables = [x // 4 for x in a]

    if any(t == 0 for t in tables):  # 어떤 색은 1테이블도 못 만듦 (a_i < 4)
        print("NE")
        return

    if sum(tables) >= n:
        print("DA")
    else:
        print("NE")

if __name__ == "__main__":
    main()
