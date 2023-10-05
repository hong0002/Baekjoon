# Bessie is planning her day of munching tender spring grass and is gazing out upon the pasture which Farmer John has so lovingly partitioned into a grid with R (1 <= R <= 100) rows and C (1 <= C <= 100) columns. She wishes to count the number of grass clumps in the pasture.
#
# Each grass clump is shown on a map as either a single '#' symbol or perhaps two '#' symbols side-by-side (but not on a diagonal). No two symbols representing two different clumps are adjacent. Given a map of the pasture, tell Bessie how many grass clumps there are.
#
# By way of example, consider this pasture map where R=5 and C=6:
#
# .#....
# ..#...
# ..#..#
# ...##.
# .#....
# This pasture has a total of 5 clumps: one on the first row, one that spans the second and third row in column 2, one by itself on the third row, one that spans columns 4 and 5 in row 4, and one more in row 5.
#
#
# Line 1: Two space-separated integers: R and C
# Lines 2..R+1: Line i+1 describes row i of the field with C characters, each of which is a '#' or a '.'
#
#
# Line 1: A single integer that is the number of grass clumps Bessie can munch

from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(matrix):
    my_queue = deque()
    visited = set()
    count = 0
    for i, i_v in enumerate(matrix):
        for j, j_v in enumerate(i_v):
            if (i, j) not in visited and j_v == '#':
                my_queue.append((i, j))
                visited.add((i, j))
                while my_queue:
                    x, y = my_queue.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < r and 0 <= ny < c and (nx, ny) not in visited:
                            if matrix[nx][ny] == '#':
                                my_queue.append((nx, ny))
                                visited.add((nx, ny))
                count += 1
    return count

r, c = map(int, input().split())
my_matrix = [[i for i in input()] for _ in range(r)]
print(bfs(my_matrix))
