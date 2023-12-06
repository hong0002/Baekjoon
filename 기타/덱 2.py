# 정수를 저장하는 덱을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
#
# 명령은 총 여덟 가지이다.
#
# 1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
# 2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
# 3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 5: 덱에 들어있는 정수의 개수를 출력한다.
# 6: 덱이 비어있으면 1, 아니면 0을 출력한다.
# 7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
# 8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
#
#
# 첫째 줄에 명령의 수 N이 주어진다. (1 ≤ N ≤ 1,000,000)
#
# 둘째 줄부터 N개 줄에 명령이 하나씩 주어진다.
#
# 출력을 요구하는 명령은 하나 이상 주어진다.
#
#
# 출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력한다.

class Deque:
    def __init__(self):
        self.data = deque()

    def append_left(self, num):
        self.data.appendleft(num)

    def append_right(self, num):
        self.data.append(num)

    def pop_left(self):
        print(self.data.popleft()) if self.deque_len() > 0 else print(-1)

    def pop_right(self):
        print(self.data.pop()) if self.deque_len() > 0 else print(-1)

    def deque_len(self):
        return len(self.data)

    def is_empty(self):
        print(1) if self.deque_len() == 0 else print(0)

    def peek_left(self):
        print(self.data[0]) if self.deque_len() > 0 else print(-1)

    def peek_right(self):
        print(self.data[self.deque_len()-1]) if self.deque_len() > 0 else print(-1)

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
my_deque = Deque()
for _ in range(n):
    op = list(map(int, input().split()))
    if op[0] == 1:
        my_deque.append_left(op[1])
    if op[0] == 2:
        my_deque.append_right(op[1])
    if op[0] == 3:
        my_deque.pop_left()
    if op[0] == 4:
        my_deque.pop_right()
    if op[0] == 5:
        print(my_deque.deque_len())
    if op[0] == 6:
        my_deque.is_empty()
    if op[0] == 7:
        my_deque.peek_left()
    if op[0] == 8:
        my_deque.peek_right()
