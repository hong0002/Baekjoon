import sys

def solve():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    t = [int(input()) for _ in range(n)]

    j = 0
    max_conc = 0
    for i in range(n):
        # t[i]와 겹치려면 t[i] - t[j] < 1000 이어야 함
        while t[i] - t[j] >= 1000:
            j += 1
        curr = i - j + 1  # 현재 동시 처리 중인 요청 수
        if curr > max_conc:
            max_conc = curr

    # 필요한 서버 수 = ceil(max_conc / k)
    ans = (max_conc + k - 1) // k
    print(ans)

if __name__ == "__main__":
    solve()
