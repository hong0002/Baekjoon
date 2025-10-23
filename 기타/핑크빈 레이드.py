import sys

def solve():
    CU, DU = map(int, sys.stdin.readline().split())
    CD, DD = map(int, sys.stdin.readline().split())
    CP, DP = map(int, sys.stdin.readline().split())
    H = int(sys.stdin.readline())

    def dmg(t: int) -> int:
        return (DU * (t // CU + 1) +
                DD * (t // CD + 1) +
                DP * (t // CP + 1))

    lo, hi = 0, H * max(CU, CD, CP)
    while lo < hi:
        mid = (lo + hi) // 2
        if dmg(mid) >= H:
            hi = mid
        else:
            lo = mid + 1
    print(lo)

if __name__ == "__main__":
    solve()
