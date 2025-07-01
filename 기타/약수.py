import sys
input = sys.stdin.readline

def main():
    k = int(input())                       # 진짜 약수의 개수
    divisors = list(map(int, input().split()))  # 진짜 약수 리스트

    # N은 최소 약수 * 최대 약수
    N = min(divisors) * max(divisors)
    print(N)

if __name__ == "__main__":
    main()
