import sys
input = sys.stdin.readline

P = int(input())
for _ in range(P):
    data = list(map(int, input().split()))
    T = data[0]
    a = data[1:]  # 길이 12
    cnt = 0
    # l은 1~10 인덱스(0-based 기준에서는 1~10), r은 l~10
    # (a[0]과 a[11]은 항상 0)
    for l in range(1, 11):
        for r in range(l, 11):
            # 구간 a[l..r]의 최소값
            seg_min = min(a[l:r+1])
            if seg_min > a[l-1] and seg_min > a[r+1]:
                cnt += 1
    print(T, cnt)
