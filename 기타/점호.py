import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    idx1 = deque()  # 창 안의 1학년 인덱스들
    idx2 = deque()  # 창 안의 2학년 인덱스들

    i = 0                  # 아직 창 안에 넣지 않은 다음 인덱스
    w = 0                  # 현재 창 안 학생 수
    target = min(K, N)     # 초기 창 크기
    while w < target:
        if A[i] == 1:
            idx1.append(i)
        else:
            idx2.append(i)
        i += 1
        w += 1

    removed = 0
    time = 0

    while removed < N:
        r = 0
        if idx1:
            idx1.popleft()
            r += 1
            removed += 1
        if idx2:
            idx2.popleft()
            r += 1
            removed += 1

        time += 1
        w -= r

        # 창을 다시 target 크기(= min(K, 남은 인원))까지 채움
        target = min(K, N - removed)
        while w < target and i < N:
            if A[i] == 1:
                idx1.append(i)
            else:
                idx2.append(i)
            i += 1
            w += 1

    print(time)

if __name__ == "__main__":
    main()
