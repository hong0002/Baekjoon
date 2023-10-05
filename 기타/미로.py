# 크기가
# $N \times M$인 미로가 있다. 미로는 격자 형태이고 .과 +로 이루어져 있다. .은 지나갈 수 있는 길을, +는 지나갈 수 없는 벽을 의미한다. 우리는 미로가 입력으로 주어지면, 미로의 두 구멍을 최단 거리로 연결할 때 지나지 않는 길을 표시할 것이다.
#
# 미로의 가장자리에 존재하는 .이 미로의 구멍이다. 항상 두 개만 주어지며, 한 구멍에서 다른 구멍으로 최단 경로로 이동해야 한다. 미로의 두 구멍은 서로 이웃하지 않는다.
#
# 두 구멍 사이를 최단 경로로 이동할 때 사용하지 않은 길은 @로 표시해야 한다.
#
# 주어진 미로를 최단 거리로 이동할 때 사용하지 않은 길을 찾는 프로그램을 작성하시오.
#
#
# 첫 번째 줄에는 미로의 크기
# $N, M$이 주어진다.
# $(3 \le N, M \le 2,001$,
# $N, M$은 홀수
# $)$ 
#
# 두 번째 줄부터는 미로의 정보가 주어진다. 두 번째 줄부터
# $N$줄에 거쳐 각 줄에는 길이가
# $M$이고 .과 +만으로 이루어진 문자열이 주어진다.
#
# 같은 지점으로 돌아오는 길이 존재하지 않고, 두 구멍 사이를 이동할 수 있는 미로만 주어진다.
#
#
# 주어진 미로를 최단 거리로 이동하는 데 사용하지 않은 길을 @로 표시한 결과를 출력한다.

import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(matrix, s):
    my_queue = deque()
    visited = set()
    a1, b1 = s[0]
    my_queue.append((a1, b1))
    matrix[a1][b1] = 0
    # 경로 찾기
    while my_queue:
        x, y = my_queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if (0 > nx or nx >= n) or (0 > ny or ny >= m) or (nx, ny) in visited:
                continue
            if matrix[nx][ny] == '@':
                matrix[nx][ny] = matrix[x][y] + 1
                my_queue.append((nx, ny))
                visited.add((nx, ny))

    # 사용한 길 . 표시하기
    visited.clear()
    a2, b2 = s[1]
    my_queue.append((a2, b2))
    while my_queue:
        x, y = my_queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if (0 > nx or nx >= n) or (0 > ny or ny >= m) or (nx, ny) in visited:
                continue
            if matrix[nx][ny] == matrix[x][y] - 1:
                my_queue.append((nx, ny))
                visited.add((nx, ny))
        matrix[x][y] = '.'

    # 사용하지 않은 길 @ 표시하기
    for i, i_v in enumerate(matrix):
        for j, j_v in enumerate(i_v):
            if j_v != '+' and j_v != '.':
                matrix[i][j] = '@'

    return matrix

n, m = map(int, input().split())
my_matrix = [list(map(lambda x: x if x == '+' else '@', list(input().rstrip()))) for _ in range(n)]

# 시작 지점과 종료 지점 찾기
idx = []
# 상단, 하단
for i in range(m):
    if len(idx) == 2: break
    if my_matrix[0][i] == '@':
        idx.append((0, i))
    if my_matrix[n-1][i] == '@':
        idx.append((n-1, i))

# 좌측, 우측
for i in range(n):
    if len(idx) == 2: break
    if my_matrix[i][0] == '@':
        idx.append((i, 0))
    if my_matrix[i][m-1] == '@':
        idx.append((i, m-1))

# 출력
for i in bfs(my_matrix, idx):
    for _, j in enumerate(i):
        print(j, end='')
    print()
