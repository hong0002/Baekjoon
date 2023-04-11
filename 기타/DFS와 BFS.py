# -*- coding: utf-8 -*-

#그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.


#첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.


#첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

import sys
from collections import deque

my_stack = deque()
my_queue = deque()
visited = deque()
n, m, v = map(int, input().split())

matrix = [[0]*(n+1) for _ in range(n+1)] # 인접행렬 기본 틀 만들기

for _ in range(m): # 간선 정보 받아서 인접행렬 만들기
    start, end = map(int, sys.stdin.readline().split())
    matrix[start][end] = 1
    matrix[end][start] = 1

my_stack.append(v) # 스택에 탐색 시작할 노드 추가

# DFS
while my_stack:
    current = my_stack.pop() # 현재 노드를 스택에서 꺼내오기
    if current not in visited: # 현재 노드가 방문하지 않았다면 방문체크
        visited.append(current)
        for destination in range(n, 0, -1): # n ~ 1까지 1씩 감소
            if matrix[current][destination] and destination not in visited: # 현재 노드에서 갈 수 있고 방문하지 않은 노드 스택에 추가
                my_stack.append(destination)

print(*visited) # 방문 순서 출력

visited.clear() # 방문 기록 초기화
my_queue.append(v) # 큐에 탐색 시작할 노드 추가

# BFS
while my_queue:
    current = my_queue.popleft() # 현재 노드를 큐에서 꺼내오기
    if current not in visited: # 현재 노드가 방문하지 않았다면 방문체크
        visited.append(current)
        for destination in range(1, n+1): # 1 ~ n 까지 (0번 인덱스에는 아무런 값도 없기 때문에 0번은 체크하지 않는다)
            if matrix[current][destination] and destination not in visited: # 현재 노드에서 갈 수 있고 방문하지 않은 노드 큐에 추가
                my_queue.append(destination)

print(*visited) # 방문 순서 출력
