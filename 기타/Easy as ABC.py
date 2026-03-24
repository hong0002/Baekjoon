grid = [input().strip() for _ in range(3)]

# 8방향
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

answer = None

def dfs(r, c, path, word):
    global answer

    if len(word) == 3:
        if answer is None or word < answer:
            answer = word
        return

    for k in range(8):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < 3 and 0 <= nc < 3 and (nr, nc) not in path:
            dfs(nr, nc, path | {(nr, nc)}, word + grid[nr][nc])

for i in range(3):
    for j in range(3):
        dfs(i, j, {(i, j)}, grid[i][j])

print(answer)
