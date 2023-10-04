# The GeoSurvComp geologic survey company is responsible for detecting underground oil de- posits. GeoSurvComp works with one large rectangular region of land at a time, and creates a grid that divides the land into numerous square plots. It then analyzes each plot separately, using sensing equipment to determine whether or not the plot contains oil. A plot containing oil is called a pocket. If two pockets are adjacent, then they are part of the same oil deposit. Oil deposits can be quite large and may contain numerous pockets. Your job is to determine how many different oil deposits are contained in a grid.


# The input file contains one or more grids. Each grid begins with a line containing m and n, the number of rows and columns in the grid, separated by a single space. If m = 0 it signals the end of the input; otherwise 1 ≤ m ≤ 100 and 1 ≤ n ≤ 100. Following this are m lines of n characters each (not counting the end-of-line characters). Each character corresponds to one plot, and is either ‘*’, representing the absence of oil, or ‘@’, representing an oil pocket.


# For each grid, output the number of distinct oil deposits. Two different pockets are part of the same oil deposit if they are adjacent horizontally, vertically, or diagonally. An oil deposit will not contain more than 100 pockets.

from collections import deque

dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(matrix):
    my_queue = deque()
    visited = set()
    count = 0
    for i, i_v in enumerate(matrix):
        for j, j_v in enumerate(i_v):
            if (i, j) not in visited and j_v == '@':
                my_queue.append((i, j))
                visited.add((i, j))
                count += 1
                while my_queue:
                    x, y = my_queue.popleft()
                    for k in range(8):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                            if matrix[nx][ny] == '@':
                                my_queue.append((nx, ny))
                                visited.add((nx, ny))
    return count

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0: break
    my_matrix = [[i for i in input()] for _ in range(m)]
    print(bfs(my_matrix))
