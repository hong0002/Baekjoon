import sys

for line in sys.stdin:
    s = line.strip()
    if s == "0":
        break

    x = int(s)
    visited = [False] * 10000
    cnt = 0

    while not visited[x]:
        visited[x] = True
        cnt += 1

        sq = x * x
        ss = f"{sq:08d}"   # 8자리 0패딩
        mid = ss[2:6]      # 가운데 4자리
        x = int(mid)

    print(cnt)
