from queue import PriorityQueue
import sys
input = sys.stdin.readline

gifts = PriorityQueue() # 우선순위 큐
n = int(input())
for _ in range(n):
    gift = list(map(int, input().split()))
    if gift[0] != 0:
        for i in range(1, len(gift)):
            gifts.put((-gift[i] ,gift[i])) # 역순으로 반환하기 위해서 튜플 형태로 저장
    else:
        if gifts.qsize() == 0: print(-1)
        else: print(gifts.get()[1])
