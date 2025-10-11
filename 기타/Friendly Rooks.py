n, m, k = map(int, input().split())
if k > min(n, m):
    print("Impossible")
else:
    print("Possible")
    board = [['.' for _ in range(m)] for _ in range(n)]
    for i in range(k):
        board[i][i] = '*'
    for row in board:
        print(''.join(row))
