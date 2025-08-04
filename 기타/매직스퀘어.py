def is_magic_square(A):
    N = len(A)
    # 1) 1~N^2가 모두 등장하는지
    nums = [x for row in A for x in row]
    if set(nums) != set(range(1, N*N + 1)):
        return False

    # 2) 목표 합 M 계산
    M = N * (N*N + 1) // 2

    # 3) 각 행의 합 검사
    for i, row in enumerate(A):
        if sum(row) != M:
            return False

    # 4) 각 열의 합 검사
    for c in range(N):
        col_sum = sum(A[r][c] for r in range(N))
        if col_sum != M:
            return False

    # 5) 두 대각선의 합 검사
    diag1 = sum(A[i][i] for i in range(N))
    diag2 = sum(A[i][N-1-i] for i in range(N))
    if diag1 != M or diag2 != M:
        return False

    return True

def main():
    import sys
    input = sys.stdin.readline

    N = int(input().strip())
    A = [list(map(int, input().split())) for _ in range(N)]

    print("TRUE" if is_magic_square(A) else "FALSE")

if __name__ == "__main__":
    main()
