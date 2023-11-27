# N×M 크기의 공간에 아기 상어 여러 마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 아기 상어가 최대 1마리 존재한다.
#
# 어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다. 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 이동은 인접한 8방향(대각선 포함)이 가능하다.
#
# 안전 거리가 가장 큰 칸을 구해보자.
#
#
# 첫째 줄에 공간의 크기 N과 M(2 ≤ N, M ≤ 50)이 주어진다. 둘째 줄부터 N개의 줄에 공간의 상태가 주어지며, 0은 빈 칸, 1은 아기 상어가 있는 칸이다. 빈 칸과 상어의 수가 각각 한 개 이상인 입력만 주어진다.
#
#
# 첫째 줄에 안전 거리의 최댓값을 출력한다.

from collections import deque

dx, dy = [-1, 0, 1, -1, 1, -1, 0, 1], [-1, -1, -1, 0, 0, 1, 1, 1]

def bfs(matrix):
    my_queue = deque()
    visited = set()
    for i, i_v in enumerate(matrix):
        for j, j_v in enumerate(i_v):
            if j_v == 1:
                my_queue.append((i, j))
                visited.add((i, j))
                matrix[i][j] = 0

    while my_queue:
        x, y = my_queue.popleft()
        for k in range(8):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                if matrix[nx][ny] == 0:
                    my_queue.append((nx, ny))
                    visited.add((nx, ny))
                    matrix[nx][ny] = matrix[x][y] + 1

    return matrix


n, m = map(int, input().split())
my_matrix = [[i for i in map(int, input().split())] for _ in range(n)]
result = 0
for i, i_v in enumerate(bfs(my_matrix)):
    for j, j_v in enumerate(i_v):
        if j_v > result:
            result = j_v
print(result)
