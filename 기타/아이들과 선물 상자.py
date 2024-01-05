# 상훈이는
# $N$개의 선물 상자를 가지고 있다. 선물 상자에는 현재 담겨있는 선물의 개수가 적혀있다.
#
# 선물을 받을 아이들이
# $M$명 있다. 아이들은 각자
# $1$에서
# $M$까지의 서로 다른 번호를 하나씩 부여받았다.
#
#  
# $1$번 아이부터
# $M$번 아이까지 한 번에 한 명씩, 현재 선물이 가장 많이 담겨있는 상자에서 각자 원하는 만큼 선물을 가져간다. 이 때, 앞서 누군가 선물을 가져갔던 선물 상자에서 또다시 가져가도 상관없다.
#
# 하지만 상자에 자신이 원하는 것보다 적은 개수의 선물이 들어있다면, 선물을 가져가지 못해 실망한다.
#
# 상훈이는 한 명이라도 실망하지 않고 모두가 선물을 가져갈 수 있는지 궁금하다.
#
#
# 첫째 줄에 선물 상자의 수
# $N$ 과 아이들의 수
# $M$이 공백을 사이에 두고 주어진다. (
# $1\le M \le N\le 10^5$)
#
# 둘째 줄에 각 선물 상자에 들어있는 선물의 개수
# $c_1,c_2,\ldots ,c_N$이 공백을 사이에 두고 주어진다. (
# $1\le c_i\le 10^5$)
#
# 셋째 줄에 아이들의 번호 순으로 각 아이가 원하는 선물의 개수
# $w_1,w_2,\ldots ,w_M$이 공백을 사이에 두고 주어진다. (
# $1\le w_i\le 10^5$)
#
#
# 모든 아이들이 실망하지 않고 각자 원하는 만큼 선물을 가져갈 수 있으면
# $1$을, 그렇지 않으면
# $0$을 출력한다.

import sys
from queue import PriorityQueue
from collections import deque
input = sys.stdin.readline

class Gift:
    def __init__(self):
        self.gifts = PriorityQueue()
        self.children = deque()

    def give_gift(self):
        while len(self.children):
            curGift = self.gifts.get()
            curChild = self.children.popleft()

            if curGift <= curChild: # 선물 개수가 원하는 선물 개수보다 많다면(-이므로 <=)
                curGift -= curChild
                self.gifts.put(curGift)
            else: return 0

        return 1

n, m = map(int, input().split())
g = list(map(int, input().split()))
c = list(map(int, input().split()))

gift = Gift()
# 내림차순으로 우선순위를 지정하기 위해 '-'사용
[gift.gifts.put(-i) for i in g]
[gift.children.append(-i) for i in c]

print(gift.give_gift())
