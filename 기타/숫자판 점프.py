# 5×5 크기의 숫자판이 있다. 각각의 칸에는 숫자(digit, 0부터 9까지)가 적혀 있다. 이 숫자판의 임의의 위치에서 시작해서, 인접해 있는 네 방향으로 다섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례로 붙이면 6자리의 수가 된다. 이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며, 0으로 시작하는 000123과 같은 수로 만들 수 있다.
#
# 숫자판이 주어졌을 때, 만들 수 있는 서로 다른 여섯 자리의 수들의 개수를 구하는 프로그램을 작성하시오.
#
#
# 다섯 개의 줄에 다섯 개의 정수로 숫자판이 주어진다.
#
#
# 첫째 줄에 만들 수 있는 수들의 개수를 출력한다.

import sys
sys.setrecursionlimit(10 ** 6) # 재귀 허용 깊이 늘림

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(x, y, number):
    number += my_matrix[x][y]
    
    # 숫자 길이가 6이면 재귀 종료 후 같은 숫자가 있는지 확인
    if len(number) == 6:
        if number not in result:
            result.append(number)
        return

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            bfs(nx, ny, number)

my_matrix = [[i for i in map(str, input().split())] for _ in range(5)]
result = []

# 모든 좌표에서 bfs 시작
for i in range(5):
    for j in range(5):
        bfs(i, j, "")

print(len(result))
