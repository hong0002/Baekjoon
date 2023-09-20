from collections import deque

def bfs():
    my_queue = deque()
    visited = set()
    count = 0
    # 모든 익은 토마토 위치 큐에 추가
    for i, i_v in enumerate(my_matrix):
        for j, j_v in enumerate(i_v):
            for k, k_v in enumerate(j_v):
                if k_v == 1:
                    my_queue.append((i, j, k))
    while my_queue:
        x, y, z = my_queue.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and (nx, ny, nz) not in visited:
                if my_matrix[nx][ny][nz] == 0:
                    my_queue.append((nx, ny, nz))
                    my_matrix[nx][ny][nz] = my_matrix[x][y][z] + 1
                    visited.add((nx, ny, nz))
                    count += 1
    return count, my_matrix

m, n, h = map(int, input().split())

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0 , 1, -1]

my_matrix = [[[i for i in map(int, input().split())] for _ in range(n)] for _ in range(h)]

bfs()

# 걸린 날짜 계산
cannot_complete = False
day = 0
for i, i_v in enumerate(my_matrix):
    for j, j_v in enumerate(i_v):
        for k, k_v in enumerate(j_v):
            if k_v == 0:
                cannot_complete = True
            day = max(day, k_v)

if cannot_complete:
    print(-1)
else:
    print(day - 1)
