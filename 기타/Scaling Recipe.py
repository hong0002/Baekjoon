import sys
input = sys.stdin.readline

def main():
    n, x, y = map(int, input().split())
    for _ in range(n):
        a = int(input())
        # 정수 결과가 보장되므로 // 사용
        print(a * y // x)

if __name__ == "__main__":
    main()
