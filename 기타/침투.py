from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(matrix):
    my_queue = deque()
    visited = set()
    for i, i_v in enumerate(matrix[0]):
        if i_v == 0:
            matrix[0][i] = 2
            my_queue.append((0, i))
            visited.add((0, i))
    while my_queue:
        x, y = my_queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = 2
                    my_queue.append((nx, ny))
                    visited.add((nx, ny))
    return matrix

m, n = map(int, input().split())
my_matrix = [[int(i) for i in input()] for _ in range(m)]
result = bfs(my_matrix)

print("YES") if 2 in result[m-1] else print("NO")

# if 2 in result[m-1]:
#     print("YES")
# else:
#     print("NO")
