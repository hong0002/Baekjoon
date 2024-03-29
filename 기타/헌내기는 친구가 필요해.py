# 2020년에 입학한 헌내기 도연이가 있다. 도연이는 비대면 수업 때문에 학교에 가지 못해 학교에 아는 친구가 없었다. 드디어 대면 수업을 하게 된 도연이는 어서 캠퍼스 내의 사람들과 친해지고 싶다.
#
# 도연이가 다니는 대학의 캠퍼스는
# $N \times M$ 크기이며 캠퍼스에서 이동하는 방법은 벽이 아닌 상하좌우로 이동하는 것이다. 예를 들어, 도연이가 (
# $x$,
# $y$)에 있다면 이동할 수 있는 곳은 (
# $x+1$,
# $y$), (
# $x$,
# $y+1$), (
# $x-1$,
# $y$), (
# $x$,
# $y-1$)이다. 단, 캠퍼스의 밖으로 이동할 수는 없다.
#
# 불쌍한 도연이를 위하여 캠퍼스에서 도연이가 만날 수 있는 사람의 수를 출력하는 프로그램을 작성해보자.
#
#
# 첫째 줄에는 캠퍼스의 크기를 나타내는 두 정수
# $N$ (
# $ 1 \leq N \leq 600$),
# $M$ (
# $ 1 \leq M \leq 600$)이 주어진다.
#
# 둘째 줄부터
# $N$개의 줄에는 캠퍼스의 정보들이 주어진다. O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐이 보장된다.
#
#
# 첫째 줄에 도연이가 만날 수 있는 사람의 수를 출력한다. 단, 아무도 만나지 못한 경우 TT를 출력한다.

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(matrix, n, m, loc):
    my_queue = deque()
    my_queue.append(loc)
    visited = set()
    visited.add(loc)
    count = 0

    while my_queue:
        x, y = my_queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                if matrix[nx][ny] == 'X':
                    continue
                if matrix[nx][ny] == 'P':
                    count += 1

                my_queue.append((nx, ny))
                visited.add((nx, ny))

    return count


n, m = map(int, input().split())
my_matrix = [list(input().rstrip()) for _ in range(n)]
loc = None

for i in range(n):
    for j in range(m):
        if my_matrix[i][j] == 'I':
            loc = (i, j)
            break

result = bfs(my_matrix, n, m, loc)

if result > 0:
    print(result)
else:
    print("TT")
