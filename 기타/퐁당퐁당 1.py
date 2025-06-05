import sys
input_data = sys.stdin.readline().split()
N = int(input_data[0])
T = int(input_data[1])

M = 2 * N
P = 2 * M - 2            # = 4*N - 2
k = (T - 1) % P

if k < M:
    ans = k + 1
else:
    ans = 2 * M - (k + 1)

print(ans)
