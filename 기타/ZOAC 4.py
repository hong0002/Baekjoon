import sys
input_data = sys.stdin.readline().split()
H, W, N, M = map(int, input_data)

rows = (H + N) // (N + 1)
cols = (W + M) // (M + 1)
print(rows * cols)
