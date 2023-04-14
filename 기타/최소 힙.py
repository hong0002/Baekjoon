# -*- coding: utf-8 -*-

#널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

#배열에 자연수 x를 넣는다.
#배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
#프로그램은 처음에 비어있는 배열에서 시작하게 된다.


#첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. x는 231보다 작은 자연수 또는 0이고, 음의 정수는 입력으로 주어지지 않는다.


#입력에서 0이 주어진 횟수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

# heapq 사용해서 구현
from heapq import heappush, heappop
from collections import deque
import sys

order_list = deque() # 입력 값을 저장하는 덱
n = int(input())

[order_list.append(int(sys.stdin.readline().rstrip())) for _ in range(n)]
min_heap = []

for order in order_list:
    if order == 0:
        if len(min_heap) == 0:
            print(0)
        else:
            print(heappop(min_heap))
    else:
        heappush(min_heap, order)


# deque를 이용해 최소힙 구현 (deque의 특성 때문에 느려서 문제에서는 시간초과가 나옴)
#from collections import deque
#import sys

#flag = True
#min_heap = deque()
#order_list = deque() # 입력 값을 저장하는 덱
#n = int(input())

#[order_list.append(int(sys.stdin.readline().rstrip())) for _ in range(n)]

#for order in order_list:
#    if order == 0: # 출력
#        if len(min_heap) == 0: # 힙이 비었다면
#            print(0)
#        else:
#            print(min_heap.popleft()) # 루트노드 출력
#            if len(min_heap) != 0: # 힙이 비지 않았을 때
#                min_heap.appendleft(min_heap.pop()) # 마지막 노드를 루트노드에 넣음
#                parent = 0
#                while flag: # 힙을 만족할 때까지 반복
#                    child = parent * 2 + 1
#                    right = parent * 2 + 1
#                    if right > len(min_heap) - 1:
#                        if child > len(min_heap) - 1: # child와 right 노드 모두 존재하지 않으면
#                            break
#                    else: # child와 right 노드가 모두 존재하면
#                        if min_heap[child] > min_heap[right]: # 오른쪽 자식이 더 작으면
#                            child = right

#                    if min_heap[child] < min_heap[parent]: # 자식 노드가 부모노드 보다 작으면
#                        min_heap[child], min_heap[parent] = min_heap[parent], min_heap[child]
#                        parent = child
#                    else:
#                        flag = False # 반복 종료
#                flag = True

#    else: # 입력
#        min_heap.append(order)
#        child = min_heap.index(order)

#        while flag:
#            parent = (child - 1) // 2
#            if min_heap[child] < min_heap[parent]: # 자식 노드가 부모노드 보다 작으면
#                min_heap[child], min_heap[parent] = min_heap[parent], min_heap[child]
#                child = parent
#                if child == 0: # 자식 노드가 루트노드라면 반복 종료
#                    break
#            else:
#                flag = False # 반복 종료
#        flag = True
            
