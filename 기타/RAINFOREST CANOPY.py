# A tropical rainforest is typically divided into four main layers: the emergent, canopy, understory, and forest floor layers. Of the four, it is quite tricky to distinguish the emergent layer from the canopy layer. The emergent layer contains a small number of very large trees, which grow above the general canopy, reaching heights of 45 to 55 metres. The canopy layer is the richest layer of the diverse rainforest, and ranges in heights of 30 to 45 metres tall. Because of bio- diversity crisis, monitoring rainforest canopy is the mission of Whole Forest Observatory, which is trying to identify suitable canopy research sites.
#
# A group of engineers have found a simple satellite imagery technique that can mark canopy layers on a spot image of a wide rainforest area. The spot image is a square and is stored as pixels, i.e., small cells containing either a 1 or a 0. Each pixel carries some information about a particular 1 km2 region. A pixel location contains a 1 if part or its entire represented region is a canopy layer and a 0 if otherwise.
#
# The following assumptions hold:
#
# A canopy layer is represented by at least a single 1.
# Cells with adjacent sides on a common pixel that contains a 1, comprise the canopy layer. A single large canopy layer image will contain all 1’s.
# Distinct canopy layers do not touch one another.
# There is no wrap-around, i.e., the pixels on the bottom are not adjacent to the top, and the left is not adjacent to the right.
# Write a program that reads spot images and correctly counts the number of canopy layers in these images.
#
#
# The input consists of up to 1000 test cases. Each test case describes a spot image of a rainforest area, which starts on a new line with a positive integer N, (1 <= N <= 40) indicating the dimension of the image. The next N lines of each test case delineate the pixelated representation of the image.
#
#
# For each test case, produce a single line of output that starts with the prefix “Case #x:” where x represents the case number (starting from one and incrementing at each new test case), followed by a single space, and then the result, i.e., the number of canopy layers in the spot image.

from collections import deque

dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(matrix):
    my_queue = deque()
    visited = set()
    count = 0
    for i, i_v in enumerate(matrix):
        for j, j_v in enumerate(i_v):
            if (i, j) not in visited and j_v == 1:
                my_queue.append((i, j))
                visited.add((i, j))
                while my_queue:
                    x, y = my_queue.popleft()
                    for k in range(8):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                            if matrix[nx][ny] == 1:
                                my_queue.append((nx, ny))
                                visited.add((nx, ny))
                count += 1
    return count

i = 1
while True:
    try:
        n = int(input())
    except:
        break
    my_matrix = [[int(i) for i in input()] for _ in range(n)]
    result = bfs(my_matrix)
    print(f"Case #{i}: {result}")
    i += 1
