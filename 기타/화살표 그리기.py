import sys
input = sys.stdin.readline

N = int(input())
colors = {}

for _ in range(N):
    x, y = map(int, input().split())
    if y not in colors:
        colors[y] = []
    colors[y].append(x)

ans = 0

for y, pos in colors.items():
    pos.sort()
    m = len(pos)
    for i in range(m):
        if i == 0:
            ans += pos[1] - pos[0]
        elif i == m - 1:
            ans += pos[m - 1] - pos[m - 2]
        else:
            ans += min(pos[i] - pos[i - 1], pos[i + 1] - pos[i])

print(ans)
