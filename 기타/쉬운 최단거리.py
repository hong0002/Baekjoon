# 지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.
#
# 문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.
#
#
# 지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)
#
# 다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개이다.
#
#
# 각 지점에서 목표지점까지의 거리를 출력한다. 원래 갈 수 없는 땅인 위치는 0을 출력하고, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.

import copy
from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(matrix, g):
    my_queue = deque()
    my_queue.append(g)
    while my_queue:
        x, y = my_queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if matrix[nx][ny] == 1:
                    my_queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return visited

n, m = map(int, input().split())
my_matrix = [[i for i in map(int, input().split())] for _ in range(n)]

goal = ()
visited = copy.deepcopy(my_matrix)
for i, i_v in enumerate(visited):
    for j, j_v in enumerate(i_v):
        if j_v == 2:
            goal = (i, j)
            visited[i][j] = 0
        elif j_v == 1:
            visited[i][j] = -1

result = bfs(my_matrix, goal)
for i in result:
    for j in i:
        print(j, end=" ")
    print("")
