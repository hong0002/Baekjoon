def make_permutation(A):
    N = len(A)
    # (값, 원래인덱스) 리스트 생성
    v = [(A[i], i) for i in range(N)]
    # 값 오름차순, 같으면 인덱스 오름차순
    v.sort(key=lambda x: (x[0], x[1]))
    # P 배열 생성
    P = [0]*N
    for sorted_pos, (_, orig_idx) in enumerate(v):
        P[orig_idx] = sorted_pos
    return P

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input().strip())
    A = list(map(int, input().split()))
    P = make_permutation(A)
    print(*P)
