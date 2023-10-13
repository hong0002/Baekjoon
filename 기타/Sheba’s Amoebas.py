# After a successful Kickstarter campaign, Sheba Arriba has raised enough money for her mail-order biology supply company. “Sheba’s Amoebas” can ship Petri dishes already populated with a colony of those tiny one-celled organisms. However, Sheba needs to be able to verify the number of amoebas her company sends out. For each dish she has a black-and-white image that has been pre-processed to show each amoeba as a simple closed loop of black pixels. (A loop is a minimal set of black pixels in which each pixel is adjacent to exactly two other pixels in the set; adjacent means sharing an edge or corner of a pixel.) All black pixels in the image belong to some loop.
#
# Sheba would like you to write a program that counts the closed loops in a rectangular array of black and white pixels. No two closed loops in the image touch or overlap. One particularly nasty species of cannibalistic amoeba is known to surround and engulf its neighbors; consequently there may be amoebas within amoebas. For instance, each of the images in Figure G.1 contains four amoebas.
#
#
# The first line of input contains two integers m and n, (1 ≤ m, n ≤ 100). This is followed by m lines, each containing n characters. A ‘#’ denotes a black pixel, a ‘.’ denotes a white pixel. For every black pixel, exactly two of its eight neighbors are also black.
#
#
# Display a single integer representing the number of loops in the input.

from collections import deque

dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(matrix):
    my_queue = deque()
    visited = set()
    count = 0
    for i, i_v in enumerate(matrix):
        for j, j_v in enumerate(i_v):
            if (i, j) not in visited and j_v == '#':
                my_queue.append((i, j))
                visited.add((i, j))
                count += 1
                while my_queue:
                    x, y = my_queue.popleft()
                    for k in range(8):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                            if matrix[nx][ny] == '#':
                                my_queue.append((nx, ny))
                                visited.add((nx, ny))
    return count

m, n = map(int, input().split())
my_matrix = [[i for i in input()] for _ in range(m)]
print(bfs(my_matrix))
