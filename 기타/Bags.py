import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    ids = list(map(int, input().split()))
    # 서로 다른 식별자의 개수를 세어 출력
    print(len(set(ids)))

if __name__ == "__main__":
    main()
