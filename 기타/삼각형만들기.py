import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    if N % 2 == 0:
        # 짝수일 때
        ans = (N * N + 24) // 48
    else:
        # 홀수일 때
        ans = ((N + 3) * (N + 3) + 24) // 48
    print(ans)

if __name__ == "__main__":
    solve()
