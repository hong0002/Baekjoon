n, m = map(int, input().split())
matrix = list()
row = 0
col = list()
[col.append(1) for _ in range(m)]
for _ in range(n):
    a = input()
    tmp = list()
    for i, v in enumerate(a):
        if v == 'X':
            col[i] = 0
        tmp.append(v)
    if 'X' not in tmp:
        row += 1
    matrix.append(tmp)

print(max(row, sum(col)))
