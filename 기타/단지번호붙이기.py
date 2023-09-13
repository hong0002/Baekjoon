# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
#
#
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
#
#
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(matrix):
    my_queue = deque()
    visited = []
    count = [-1 for _ in range(n*n)]
    idx = 0
    for i, i_v in enumerate(matrix):
        for j, v_j in enumerate(i_v):
            if (i, j) not in visited and v_j == 1: # 방문하지 않고 1인 것들
                my_queue.append((i, j))
                while my_queue:
                    x, y = my_queue.popleft()
                    count[idx] += 1
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                            if matrix[nx][ny] == 1:
                                my_queue.append((nx, ny))
                                visited.append((nx, ny))
                idx += 1
    return count

n = int(input())
my_matrix = [[i for i in map(int, input().rstrip())] for _ in range(n)]
c = bfs(my_matrix)

# -1인 리스트 제거
remove_set = {-1}
c = [i for i in c if i not in remove_set]
# 0인 리스트 값 1로 변경
c = [1 if x==0 else x for x in c]
c.sort()
print(len(c))
[print(i) for i in c]
