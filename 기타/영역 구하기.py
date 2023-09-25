# 눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.
#
# 예를 들어 M=5, N=7 인 모눈종이 위에 <그림 1>과 같이 직사각형 3개를 그렸다면, 그 나머지 영역은 <그림 2>와 같이 3개의 분리된 영역으로 나누어지게 된다.
#
# <그림 2>와 같이 분리된 세 영역의 넓이는 각각 1, 7, 13이 된다.
#
# M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.
#
#
# 첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다. 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다. 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.
#
#
# 첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.

from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(matrix):
    my_queue = deque()
    visited = set()
    counts = []
    for i, i_v in enumerate(matrix):
        for j, j_v in enumerate(i_v):
            if (i, j) not in visited and j_v == 0:
                my_queue.append((i, j))
                count = 0
                while my_queue:
                    x, y = my_queue.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                            if matrix[nx][ny] == 0:
                                my_queue.append((nx, ny))
                                visited.add((nx, ny))
                                count += 1
                if count == 0:
                    count = 1
                counts.append(count)
    return counts

m, n, k = map(int, input().split())
my_matrix = [[0 for _ in range(m)] for _ in range(n)]

# 직사각형 그리기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            my_matrix[i][j] = 1

result = bfs(my_matrix)
result.sort()
print(len(result))
[print(i, end=" ") for i in result]
