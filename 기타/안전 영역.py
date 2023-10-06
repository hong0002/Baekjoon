from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(matrix):
    island = []
    for h in range(100):
        my_queue = deque()
        visited = set()
        count = 0
        for i, i_v in enumerate(matrix):
            for j, j_v in enumerate(i_v):
                if (i, j) not in visited and j_v > h:
                    my_queue.append((i, j))
                    while my_queue:
                        x, y = my_queue.popleft()
                        for k in range(4):
                            nx, ny = x+dx[k], y+dy[k]
                            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                                if matrix[nx][ny] > h:
                                    my_queue.append((nx, ny))
                                    visited.add((nx, ny))
                    count += 1
        island.append(count) # 섬의 개수 만큼 리스트에 저장
    return island

n = int(input())
my_matrix = [[i for i in map(int, input().split())] for _ in range(n)]
print(max(bfs(my_matrix)))
