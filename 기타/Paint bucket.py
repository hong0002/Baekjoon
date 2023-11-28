# One of the most time-saving operations when drawing on a computer (for example using Photoshop) is the “bucket fill”  operation.
#
# When you select this tool and click on a (target) pixel of the image it will fill all the pixels that have the same color than the target pixel and are connected to it. Two pixels are connected if they share a side or if they are connected through a path of connected pixels.
#
# Let’s see an example: In the following image, if we select the “fill” operation in an image editor program and click on the center of the image (orange pixel). The whole region will be painted orange. Notice that the pixels are not connected diagonally so two corners of the image remain white.
#
# Your task is: Given a matrix of digits representing the pixels, simulated what would be the result of a “fill” operation on given pixels. Thus, the colors will be represented with a number from 0 to 9.
#
# Let’s see another example, now using digits instead of pixels. We have the following image:
#
# 0000000
# 0111000
# 0111010
# 0000000
# If we “fill” at position Y = 0, X = 0 with color 3, all the 0s get painted of color 3. Because all of them are recursively connected.
#
# The result will be:
#
# 3333333
# 3111333
# 3111313
# 3333333
#
#
# The first line will contain two integers R and C representing the number of rows and columns of the image.
#
# The next R lines will contain C digits each representing the initial colors of the pixels.
#
# The last line will contain 3 integers Y, X and K representing the row and column where we want to apply the “fill” operation and the color to use.
#
# The images will be smaller than 1000 x 1000 pixels.
#
# The colors are limited to a single digit from 0 to 9.
#
#
# Print the resulting image after applying the operation in the same format as the input.

from collections import deque

da, db = [0, 0, -1, 1], [1, -1, 0, 0]

def bfs(matrix):
    my_queue = deque()
    visited = set()
    color = matrix[y][x]
    matrix[y][x] = k
    my_queue.append((y, x))
    visited.add((y, x))
    while my_queue:
        a, b = my_queue.popleft()
        for i in range(4):
            na, nb = a+da[i], b+db[i]
            if 0 <= na < r and 0 <= nb < c and (na, nb) not in visited:
                if matrix[na][nb] == color:
                    my_queue.append((na, nb))
                    visited.add((na, nb))
                    matrix[na][nb] = k
    return matrix

r, c = map(int, input().split())
my_matrix = [[int(i) for i in input()] for _ in range(r)]
y, x, k = map(int, input().split())
for i in bfs(my_matrix):
    for j in i:
        print(j, end="")
    print()
