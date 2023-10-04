# There is a rectangular room, covered with square tiles. Each tile is colored either red or black. A man is standing on a black tile. From a tile, he can move to one of four adjacent tiles. But he can't move on red tiles, he can move only on black tiles.
#
# Write a program to count the number of black tiles which he can reach by repeating the moves described above.
#
#
# The input consists of multiple data sets. A data set starts with a line containing two positive integers W and H; W and H are the numbers of tiles in the x- and y- directions, respectively. W and H are not more than 20.
#
# There are H more lines in the data set, each of which includes W characters. Each character represents the color of a tile as follows.
#
# '.' - a black tile
# '#' - a red tile
# '@' - a man on a black tile(appears exactly once in a data set)
# The end of the input is indicated by a line consisting of two zeros.
#
#
# For each data set, your program should output a line which contains the number of tiles he can reach from the initial tile (including itself).

from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(matrix):
    my_queue = deque()
    visited = set()
    for i, i_v in enumerate(matrix):
        for j, j_v in enumerate(i_v):
            if j_v == '@':
                my_queue.append((i, j))
                visited.add((i, j))
    count = 0
    while my_queue:
        x, y = my_queue.popleft()
        count += 1
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < h and 0 <= ny < w and (nx, ny) not in visited:
                if matrix[nx][ny] == '.':
                    my_queue.append((nx, ny))
                    visited.add((nx, ny))
    return count

while True:
    w, h = map(int, input().split())
    if w == 0  and h == 0: break
    my_matrix = [[i for i in input()] for _ in range(h)]
    print(bfs(my_matrix))
