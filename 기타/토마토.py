import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(matrix):
    my_queue = deque()
    visited = set()
    count = 0
    # 1이 있는 위치 찾아서 my_queue에 append
    for i, i_v in enumerate(matrix):
        for j, j_v in enumerate(i_v):
            if j_v == 1:
                my_queue.append((i, j))
    while my_queue:
        x, y = my_queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = matrix[x][y] + 1
                    my_queue.append((nx, ny))
                    visited.add((nx, ny))
                    count += 1
    return count, matrix

m, n = map(int, input().split())
my_matrix = [[i for i in map(int, input().split())] for _ in range(n)]

# 토마토 수 세기
tomatos = 0
for _, i_v in enumerate(my_matrix):
    for _, j_v in enumerate(i_v):
        if j_v == 0:
            tomatos += 1

a, b = bfs(my_matrix)
if tomatos == a:
    print(max(map(max, b)) - 1)
else:
    print(-1)
