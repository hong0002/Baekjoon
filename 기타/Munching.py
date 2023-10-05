# Bessie loves her grass and loves to hurry to the barn for her evening milking session. She has partitioned the pasture into a rectilinear grid of R (1 <= R <= 100) rows and C (1 <= C <= 100) columns and marked the squares as grass or rocky (she can't eat rocks and won't even go into those squares). Bessie starts on her map at location R_b,C_b and wishes to munch her way, square by square, to the barn at location 1,1 by the shortest route possible. She moves from one square to any one of the potentially four adjacent squares.
#
# Below is the original map [with rocks ('*'), grass ('.'), the barn ('B'), and Bessie ('C' for cow) at row 5, col 6] and a route map with the optimal route marked with munches ('m'):
#
#            Map               Optimal Munched Route
#         1 2 3 4 5 6  <-col      1 2 3 4 5 6  <-col
#       1 B . . . * .           1 B m m m * .
#       2 . . * . . .           2 . . * m m m
#       3 . * * . * .           3 . * * . * m
#       4 . . * * * .           4 . . * * * m
#       5 * . . * . C           5 * . . * . m
# Bessie munched 9 squares.
#
# Given a map, determine how many squares Bessie will eat on her shortest route to the barn (there's no grass to eat on the barn's square).
#
#
# Line 1: Two space-separated integers: R and C
# Lines 2..R+1: Line i+1 describes row i with C characters (and no spaces) as described above
#
#
# Line 1: A single integer that is the number of squares of grass that Bessie munches on the shortest route back to the barn

from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(matrix):
    my_queue = deque()
    visited = set()
    for i, i_v in enumerate(matrix):
        for j, j_v in enumerate(i_v):
            if j_v == 'B':
                my_queue.append((i, j))
                visited.add((i, j))
                matrix[i][j] = 0
                while my_queue:
                    x, y = my_queue.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < r and 0 <= ny < c and (nx, ny) not in visited:
                            if matrix[nx][ny] == '.' or matrix[nx][ny] == 'C':
                                if matrix[nx][ny] == 'C':
                                    return matrix[x][y] + 1
                                matrix[nx][ny] = matrix[x][y] + 1
                                my_queue.append((nx, ny))
                                visited.add((nx, ny))

r, c = map(int, input().split())
my_matrix = [[i for i in input()] for _ in range(r)]
print(bfs(my_matrix))
