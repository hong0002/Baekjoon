import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    days = list(map(int, input().split()))
    # days는 오름차순으로 주어짐 (문제 조건)

    # 모든 날을 1일 구독으로 시작
    total = N + N * K  # (1+K) * N

    # 인접한 시청일 사이의 갭을 보고, 갭 < K인 경우 합침
    for i in range(N - 1):
        gap = days[i + 1] - days[i] - 1  # 사이에 비는 날 수
        if gap < K:
            total += gap - K  # 합치면 K 절약, gap만큼 길이 비용 추가

    print(total)

if __name__ == "__main__":
    main()
