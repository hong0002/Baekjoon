# -*- coding: utf-8 -*-

#가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.


#첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다. i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다. i번째 줄의 i번째 숫자는 항상 0이다.


#총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다. 정점 i에서 j로 가는 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.

import sys
from collections import deque

count = int(0)
my_stack = deque()
visited = deque()

n = int(input())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 인접행렬 받기
result_matrix = [[0]*n for _ in range(n)] # 결과 인접행렬 기본 틀

# DFS
for i in range(n):
    my_stack.append(i)
    while my_stack:
        current = my_stack.pop()
        if current not in visited:
            if count != 0: # 처음 노드는 방문한 것으로 치지 않음
                visited.append(current)
                result_matrix[i][current] = 1
            for destination in range(n):
                if matrix[current][destination] and destination not in visited:
                    my_stack.append(destination)
        count += 1
    count = 0
    visited.clear()

for i in range(n): # 출력
    [print(result_matrix[i][j], end=" ") for j in range(n)]
    print()
