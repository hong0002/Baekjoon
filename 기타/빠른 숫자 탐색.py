# 5 x 5 크기의 보드가 주어진다. 보드는 1 x 1 크기의 정사각형 격자로 이루어져 있다. 보드의 격자에는 -1, 0, 1중 하나의 숫자가 적혀 있다. 격자의 위치는 (r, c)로 표시한다. r은 행 번호, c는 열 번호를 나타낸다. 행 번호는 맨 위 위치가 0이고 아래 방향으로 1씩 증가한다. 열 번호는 맨 왼쪽 위치가 0이고 오른쪽 방향으로 1씩 증가한다. 즉, 맨 왼쪽 위 위치가 (0, 0), 맨 아래 오른쪽 위치가 (4, 4)이다. -1이 적혀 있는 칸으로는 이동할 수 없고 0, 1이 적혀 있는 칸으로는 이동할 수 있다.
#
# 현재 한 명의 학생이 (r, c) 위치에 있고 한 번의 이동으로 상, 하, 좌, 우 방향 중에서 한 방향으로 한 칸 이동할 수 있다. 학생이 현재 위치 (r, c)에서 시작하여 1이 적혀 있는 칸에 도착하기 위한 최소 이동 횟수를 출력하자. 현재 위치 (r, c)에서 시작하여 1이 적혀 있는 칸으로 이동할 수 없는 경우 –1을 출력한다. 보드에는 1이 적혀 있는 격자가 1개 주어진다.
#
#
# 첫 번째 줄부터 다섯 개의 줄에 걸쳐 보드의 정보가 순서대로 주어진다. i번째 줄의 j번째 숫자는 보드의 (i - 1)번째 행, (j - 1)번째 열의 정보를 나타낸다. 보드의 정보는 -1, 0, 1중 하나이다.
#
# 다음 줄에 학생의 현재 위치 r, c가 빈칸을 사이에 두고 순서대로 주어진다.
#
#
# 학생이 현재 위치 (r, c)에서 1이 적혀 있는 칸에 도착하기 위한 최소 이동 횟수를 출력한다. 현재 위치 (r, c)에서 1이 적혀 있는 칸으로 이동할 수 없는 경우 -1을 출력한다.

from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(matrix, s, a, b):
    my_queue = deque()
    visited = set()
    my_queue.append(s)
    while my_queue:
        x, y = my_queue.popleft()
        visited.add((x, y))
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in visited:
                if matrix[nx][ny] != -1:
                    my_queue.append((nx, ny))
                    matrix[nx][ny] = matrix[x][y] + 1

    return matrix[a][b]

my_matrix = [[i for i in map(int, input().split())] for _ in range(5)]
start = tuple(map(int, input().split()))
a, b = 0, 0
for i, i_v in enumerate(my_matrix):
    for j, j_v in enumerate(i_v):
        if j_v == 1:
            a, b = i, j
            my_matrix[i][j] = '#'
            break

result = bfs(my_matrix, start, a, b)
print(-1) if result == '#' else print(result)
