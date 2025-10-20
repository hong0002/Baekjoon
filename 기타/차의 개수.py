import sys

def solve():
    N = int(sys.stdin.readline().strip())

    # 최대: 골롬자(ruler) 성질을 갖는 {1,2,4,...,2^{N-1}}
    max_count = N * (N - 1) // 2
    max_seq = [1 << i for i in range(N)]  # 1,2,4,...,2^{N-1}

    # 최소: 등차수열 {1,2,...,N}
    min_count = N - 1
    min_seq = list(range(1, N + 1))

    print(max_count)
    print(*max_seq)
    print(min_count)
    print(*min_seq)

if __name__ == "__main__":
    solve()
