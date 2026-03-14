import sys
input = sys.stdin.readline

R, C = map(int, input().split())
N = int(input())

INF = 10**18

min_r = [INF] * (N + 1)
max_r = [0] * (N + 1)
min_c = [INF] * (N + 1)
max_c = [0] * (N + 1)
exists = [False] * (N + 1)

for _ in range(N):
    a, v, h = map(int, input().split())
    exists[a] = True
    if v < min_r[a]:
        min_r[a] = v
    if v > max_r[a]:
        max_r[a] = v
    if h < min_c[a]:
        min_c[a] = h
    if h > max_c[a]:
        max_c[a] = h

best_id = -1
best_area = -1

for a in range(1, N + 1):
    if not exists[a]:
        continue
    area = (max_r[a] - min_r[a] + 1) * (max_c[a] - min_c[a] + 1)
    
    if area > best_area or (area == best_area and a < best_id):
        best_area = area
        best_id = a

print(best_id, best_area)
