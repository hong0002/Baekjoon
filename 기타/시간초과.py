import sys

input = sys.stdin.readline

C = int(input())

for _ in range(C):
    S, N, T, L = input().split()
    N = int(N)
    T = int(T)
    L = int(L)

    limit = L * 100000000
    allowed = limit // T  # f(N)이 이 값 이하이면 통과

    ok = True

    if S == "O(N)":
        val = N
        ok = (val <= allowed)

    elif S == "O(N^2)":
        val = N * N
        ok = (val <= allowed)

    elif S == "O(N^3)":
        val = N * N * N
        ok = (val <= allowed)

    elif S == "O(2^N)":
        val = 1
        for _ in range(N):
            val *= 2
            if val > allowed:
                ok = False
                break
        else:
            ok = True

    elif S == "O(N!)":
        val = 1
        for i in range(1, N + 1):
            val *= i
            if val > allowed:
                ok = False
                break
        else:
            ok = True

    print("May Pass." if ok else "TLE!")
