import sys

def main():
    input = sys.stdin.readline
    n = int(input().strip())

    arrival = [0] * (n + 1)
    for _ in range(n):
        t, idx = map(int, input().split())
        arrival[idx] = t

    # A[i] = max(arrival[1..i])
    A = [0] * (n + 1)
    for i in range(1, n + 1):
        A[i] = max(A[i - 1], arrival[i])

    cur = 1          # 다음 패킷을 재생하려는 시각(초의 시작)
    lag = 0

    for i in range(1, n + 1):
        if cur < A[i]:
            lag += A[i] - cur
            cur = A[i]
        cur += 1     # 패킷 i를 1초 동안 재생

    print(lag)

if __name__ == "__main__":
    main()
