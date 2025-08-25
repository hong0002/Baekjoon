import sys

input = sys.stdin.readline

N = int(input().strip())
points = []
for idx in range(1, 3 * N + 1):
    x, y = map(int, input().split())
    points.append((x, y, idx))  # (x, y, original_index)

# x 오름차순, x가 같으면 y 오름차순
points.sort(key=lambda p: (p[0], p[1]))

# 앞에서부터 3개씩 묶어 출력
for i in range(N):
    a = points[3*i][2]
    b = points[3*i + 1][2]
    c = points[3*i + 2][2]
    print(a, b, c)
