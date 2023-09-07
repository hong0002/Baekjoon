# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
#
#
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
#
#
# 첫째 줄에 연결 요소의 개수를 출력한다.

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
my_queue = deque()
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

start_list = [i for i in range(1, n+1)]
visited = []

count = 0
while start_list:
    current = start_list[0]
    my_queue.append(current)
    visited = [current]
    start_list.remove(current)
    while my_queue:
        current = my_queue.popleft()
        for i in graph[current]:
            if i not in visited:
                visited.append(i)
                my_queue.append(i)
                start_list.remove(i)
    count += 1
print(count)
