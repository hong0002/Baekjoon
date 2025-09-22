import sys

def main():
    input = sys.stdin.readline
    N, T = map(int, input().split())
    # 시간 상한이 1000이므로 [0, 1000] 경계 포함 차분배열은 넉넉히 1002
    diff = [0] * 1002

    for _ in range(N):
        K = int(input())
        for _ in range(K):
            S, E = map(int, input().split())
            # 구간 [S, E) 참석 가능
            diff[S] += 1
            diff[E] -= 1

    # cover[t] = [t, t+1) 구간에 가능한 인원 수
    cover = [0] * 1001  # t=0..1000-1 사용
    cur = 0
    for t in range(1001):  # 0..1000
        cur += diff[t]
        if t < 1000:
            cover[t] = cur

    # prefix sum: ps[i] = sum_{t=0}^{i-1} cover[t]
    ps = [0] * (1001)
    for t in range(1000):
        ps[t+1] = ps[t] + cover[t]

    # 길이 T 창 슬라이딩
    best_s = 0
    best_val = -1
    last_start = 1000 - T
    if last_start < 0:
        # T가 너무 큰 경우는 조건상 나오지 않지만 방어
        last_start = 0

    for s in range(0, last_start + 1):
        val = ps[s+T] - ps[s]
        if val > best_val:
            best_val = val
            best_s = s

    print(best_s, best_s + T)

if __name__ == "__main__":
    main()
