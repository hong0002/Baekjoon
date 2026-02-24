import sys
import math

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    M, N, x, y = map(int, input().split())

    lcm = M * N // math.gcd(M, N)
    ans = -1

    # k는 x를 만족하는 해들만 확인
    k = x
    while k <= lcm:
        # 카잉 달력에서 N쪽 값 계산 (1~N)
        ky = k % N
        if ky == 0:
            ky = N

        if ky == y:
            ans = k
            break

        k += M

    print(ans)
