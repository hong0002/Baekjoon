# It's Bessie's feeding time, and Farmer John is trying to decide where to put her. FJ has a farm that comprises W x H (1 <= W <= 750; 1 <= H <= 750) squares and is partitioned into one or more separate pastures by rocks both large and small. Every pasture contains some grass and some rocks.
#
# Bessie is a hungry little cow and just loves to eat, eat, eat her grass. She can move from any square to any other square that is horizontally, vertically, or diagonally adjacent. Bessie can't cross the rocks because they hurt her feet, and, of course, she can't leave the farm. Bessie wants to know the maximum number of squares of grass that she can eat.
#
# FJ has a map of his farm, where a '.' represents a square of grass, and a '*' represents a rock. Consider this 10x8 map and a detailed breakdown of the extent of each of its three pastures:
#
#       ...*....**  |  111*....**   ...*2222**    ...*....**
#       ..**....**  |  11**....**   ..**2222**    ..**....**
#       ...*....**  |  111*....**   ...*2222**    ...*....**
#       ...**.*.**  |  111**.*.**   ...**2*2**    ...**.*.**
#       ***.**.***  |  ***1**.***   ***.**2***    ***.**.***
#       ...**.*.**  |  111**.*.**   ...**2*2**    ...**.*.**
#       ...*.*****  |  111*.*****   ...*2*****    ...*.*****
#       ...***..**  |  111***..**   ...***..**    ...***33**
# Pasture 1 has 21 squares; pasture 2 has 18 squares; pasture 3 has 2 squares. Thus Bessie should choose pasture 1 with 21 squares to maximize the grass she can eat.
#
#
# Line 1: Two space-separated integers: W and H
# Lines 2..H+1: Line i+1 describes field row i with W characters (and no spaces), each either '.' or '*'
#
#
# Line 1: A single integer that represents the maximum number of squares of grass that Bessie can eat.

from collections import deque

dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(matrix):
    my_queue = deque()
    visited = set()
    counts = []
    for i, i_v in enumerate(matrix):
        for j, j_v in enumerate(i_v):
            if (i, j) not in visited and j_v == '.':
                my_queue.append((i, j))
                visited.add((i, j))
                count = 0
                while my_queue:
                    x, y = my_queue.popleft()
                    count += 1
                    for k in range(8):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < h and 0 <= ny < w and (nx, ny) not in visited:
                            if matrix[nx][ny] == '.':
                                my_queue.append((nx, ny))
                                visited.add((nx, ny))
                counts.append(count)
    return max(counts)

w, h = map(int, input().split())
my_matrix = [[i for i in input()] for _ in range(h)]
print(bfs(my_matrix))
