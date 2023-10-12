# There are a lot of elephants in Chiang Mai and many elephant camps can be seen around this city. Elephant camps are among the most popular attractions in Chiang Mai, but Khun-LungKen Elephant Farm is very different from the others.
#
# At Khun-Lung-Ken Elephant Farm you can enjoy shows performed by elephants such as dancing, playing football and painting. But the most interesting show is when an elephant eats apples on the ground at high speed. This show is held on a rectangular ground, which is covered with big square tiles. Each tile is colored in either red or yellow, and each tile has an apple placed on it. At first an elephant stands on a yellow tile. From this tile, he can move to one of four adjacent tiles. However, he can only move horizontally or vertically. Unbelievably, he will not move on red tiles, he will only move on yellow tiles in order to get an apple, and will never pick up an apple placed on a red tile.
#
# Write a program to count the number of apples which the elephant can eat by repeating the moves described above.
#
#
# The input consists of multiple data sets. A data set starts with a line containing two positive integers W and H; W and H are the numbers of tiles in the x- and y- directions, respectively. W and H are not more than 40.
#
# There are H lines in the data set, each of which includes W characters. Each character represents the color of a tile as follows.
#
# '.' → a yellow tile
# '#' → a red tile
# 'A' → an elephant on a yellow tile (appears once in the data set)
# The end of the input is indicated when both W and H are Zero.
#
#
# For each data set, your program should output a line which contains the number of tiles the elephant can reach from the initial tile (including this tile).

from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(matrix):
    my_queue = deque()
    visited = set()
    count = 0
    for i, i_v in enumerate(matrix):
        for j, j_v in enumerate(i_v):
            if j_v == 'A':
                my_queue.append((i, j))
                visited.add((i, j))
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
    if w == 0 and h == 0: break
    my_matrix = [[i for i in input()] for _ in range(h)]
    print(bfs(my_matrix))
