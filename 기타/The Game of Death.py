import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    A = [0] * (N + 1)

    for i in range(1, N + 1):
        A[i] = int(input())

    visited = [False] * (N + 1)
    cur = 1
    k = 0
    answer = 0

    while True:
        if visited[cur]:
            answer = 0
            break
        visited[cur] = True

        cur = A[cur]
        k += 1

        if cur == N:
            answer = k
            break

    print(answer)
