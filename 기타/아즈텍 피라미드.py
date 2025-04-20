import sys

def max_height(n: int) -> int:
    # f(L) = (2L^3 + L) / 3 <= n  <=>  2L^3 + L <= 3n
    lo, hi = 0, int((1.5 * n) ** (1/3)) + 3
    # hi가 부족할 경우 두 배씩 늘려주기
    while 2*hi**3 + hi <= 3*n:
        hi *= 2
    # [lo, hi) 구간에서 이진 탐색
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if 2*mid**3 + mid <= 3*n:
            lo = mid
        else:
            hi = mid
    return lo

def main():
    n = int(sys.stdin.readline().strip())
    print(max_height(n))

if __name__ == "__main__":
    main()
