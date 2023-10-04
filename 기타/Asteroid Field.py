# Plot a path through the asteroid field. Given a starting location, final destination, and a description of the asteroid fields plot a shortest path that takes you from the starting location to the final destination without running into any asteroids. The asteroid field is described using a mxm grid of characters with
#
# s: for starting location
# d: for final location
# -: for open space
# *: asteroid
# Here is an example of a 4x4 grid.
#
# s*-*
# -*-*
# ----
# *-*d
# Your ship can move up, down, left, and right (not diagonally). Each position in a mxm grid will be assigned an integer between 0 and m2-1 as follows.
#
#
# The first line will have a positive integer n representing the number of data sets. The first line of each data set will contain an integer m, followed by m lines, and each line will contain m characters. The character s will always be in the top left corner and d will always be in the bottom right corner.
#
#
# For each data set print the minimal number of moves needed to reach the destination or -1 if there is no solution.

from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(matrix):
    my_queue = deque()
    visited = set()
    my_queue.append((0, 0))
    matrix[0][0] = 0
    while my_queue:
        x, y = my_queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < m and 0 <= ny < m and (nx, ny) not in visited:
                if matrix[nx][ny] == '-' or matrix[nx][ny] == 'd':
                    matrix[nx][ny] = matrix[x][y] + 1
                    my_queue.append((nx, ny))
                    visited.add((nx, ny))
    return matrix[m-1][m-1]

n = int(input())
for _ in range(n):
    m = int(input())
    my_matrix = [[i for i in input()] for _ in range(m)]
    result = bfs(my_matrix)
    print(-1) if result == 'd' else print(result)
