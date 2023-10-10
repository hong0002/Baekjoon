# A robot is stuck in a maze with multiple exits and needs to find the shortest path out. The maze can be represented as a two dimensional grid where each space is either a wall, which the robot cannot go through, an exit, or one of the goals. The robot can only move one space at a time, and at each move it can only move either horizontally or vertically, not diagonally. It can exit the maze from any exit, but it needs to start at the specified place. What is the fewest number of moves the robot can make to exit from the maze?
#
#
# The input will be given first by a number that tells the number of different mazes in the input file. Following that, for each data set, there will be two integers, R and C. The first number, R, represents the number or rows in the maze, and the second number, C, representing the number of columns. The following R lines will each be a series of characters representing spaces on the grid for that row. An X will represent an obstacle, and 'O' or '0' will represent an open space that the robot can move. An S will represent the starting location of the robot. The goals in the maze will be given by the letter G. There may be more than one goal.
#
#
# The output should be if the robot can get out of the maze:
#
# “Shortest Path: t”
#
# Where t is an integer representing the length of the shortest path. If there is no way out of the maze, the output should be:
#
# “No Exit”
#
# Each line of output should be printed at the end of the program.

from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(matrix):
    my_queue = deque()
    visited = set()
    goals = []
    for i, i_v in enumerate(matrix):
        for j, j_v in enumerate(i_v):
            if j_v == 'S':
                my_queue.append((i, j))
                matrix[i][j] = 0
            elif j_v == 'G':
                goals.append((i, j))
    while my_queue:
        x, y = my_queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < r and 0 <= ny < c and (nx, ny) not in visited:
                if matrix[nx][ny] == 'O' or matrix[nx][ny] == 'G' or matrix[nx][ny] == '0':
                    matrix[nx][ny] = matrix[x][y] + 1
                    my_queue.append((nx, ny))
                    visited.add((nx, ny))
    path = []
    for l in goals:
        a, b = l
        if matrix[a][b] != 'G':
            path.append(matrix[a][b])
    return path

n = int(input())
for _ in range(n):
    r, c = map(int, input().split())
    my_matrix = [[i for i in input()] for _ in range(r)]
    result = bfs(my_matrix)
    print("Shortest Path:", min(result)) if result else print("No Exit")
