# 전쟁은 어느덧 전면전이 시작되었다. 결국 전투는 난전이 되었고, 우리 병사와 적국 병사가 섞여 싸우게 되었다. 그러나 당신의 병사들은 흰색 옷을 입고, 적국의 병사들은 파란색 옷을 입었기 때문에 서로가 적인지 아군인지는 구분할 수 있다. 문제는 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다.
#
# N명이 뭉쳐있을 때는 N2의 위력을 낼 수 있다. 과연 지금 난전의 상황에서는 누가 승리할 것인가? 단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.
#
#
# 첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다. 그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다. 모든 자리에는 병사가 한 명 있다. B는 파란색, W는 흰색이다. 당신의 병사와 적국의 병사는 한 명 이상 존재한다.
#
#
# 첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력한다.

from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(start, color):
    my_queue = deque()
    my_queue.append(start)
    count = 0
    while my_queue:
        x, y = my_queue.popleft()
        count += 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                if my_matrix[nx][ny] == color:
                    my_queue.append((nx, ny))
                    visited.add((nx, ny))
    return count - 1

n, m = map(int, input().split())

my_matrix = [[i for i in input()] for _ in range(m)]
visited = set()

w_count = 0
b_count = 0
for i, i_v in enumerate(my_matrix):
    for j, j_v in enumerate(i_v):
        if (i, j) not in visited:
            if j_v == 'W':
                c = bfs((i, j), j_v)
                if c == 0:
                    w_count += 1
                else:
                    w_count += pow(c, 2)
            elif j_v == 'B':
                c = bfs((i, j), j_v)
                if c == 0:
                    b_count += 1
                else:
                    b_count += pow(c, 2)

print(w_count, b_count)
