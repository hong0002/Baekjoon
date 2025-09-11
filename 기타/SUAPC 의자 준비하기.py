N, M, A, B = map(int, input().split())
K = max(0, 3*N - M)
print(0 if K == 0 else K*A + B)
