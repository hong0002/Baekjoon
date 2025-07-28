import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    total_qaly = 0.0

    for _ in range(N):
        q, y = map(float, input().split())
        total_qaly += q * y

    # 소수점 셋째 자리까지 출력
    print(f"{total_qaly:.3f}")

if __name__ == "__main__":
    main()
