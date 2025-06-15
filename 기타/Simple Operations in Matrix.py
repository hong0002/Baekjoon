def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    Q = int(input())
    for _ in range(Q):
        typ, k, val = input().split()
        k = int(k) - 1
        val = int(val)
        if typ == 'row':
            # k번째 행 전체에 val 더하기
            for j in range(M):
                A[k][j] += val
        else:  # 'col'
            # k번째 열 전체에 val 더하기
            for i in range(N):
                A[i][k] += val

    total = 0
    mn = float('inf')
    mx = -float('inf')
    for i in range(N):
        for j in range(M):
            x = A[i][j]
            total += x
            if x < mn: mn = x
            if x > mx: mx = x

    print(total, mn, mx)

if __name__ == "__main__":
    main()
