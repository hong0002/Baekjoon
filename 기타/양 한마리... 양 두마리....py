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
                        if 0 <= nx < h and 0 <= ny < w and (nx, ny) not in visited:
                            if matrix[nx][ny] == '#':
                                my_queue.append((nx, ny))
                                visited.add((nx, ny))
                count += 1
    return count

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    my_matrix = [[i for i in input()] for _ in range(h)]
    print(bfs(my_matrix))
