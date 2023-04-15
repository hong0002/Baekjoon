# -*- coding: utf-8 -*-

#절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

#배열에 정수 x (x ≠ 0)를 넣는다.
#배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
#프로그램은 처음에 비어있는 배열에서 시작하게 된다.


#첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 정수는 -231보다 크고, 231보다 작다.


#입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

from heapq import heappop, heappush
import sys

n = int(input())

order_list = []
[order_list.append(int(sys.stdin.readline().rstrip())) for _ in range(n)] # 명령 리스트 추가

abs_heap = [] # 절댓값 힙
for order in order_list:
    if order == 0: # 출력
        if abs_heap:
            print(heappop(abs_heap)[1])
        else:
            print(0)
    else: # 입력
        abs_order = abs(order) # order의 절댓값 구하기
        heappush(abs_heap, (abs_order, order)) # (절댓값, 원래 값) 모양으로 abs_heap에 push
