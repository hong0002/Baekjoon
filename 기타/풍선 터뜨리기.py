# 1번부터 N번까지 N개의 풍선이 원형으로 놓여 있고. i번 풍선의 오른쪽에는 i+1번 풍선이 있고, 왼쪽에는 i-1번 풍선이 있다. 단, 1번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있다. 각 풍선 안에는 종이가 하나 들어있고, 종이에는 -N보다 크거나 같고, N보다 작거나 같은 정수가 하나 적혀있다. 이 풍선들을 다음과 같은 규칙으로 터뜨린다.
#
# 우선, 제일 처음에는 1번 풍선을 터뜨린다. 다음에는 풍선 안에 있는 종이를 꺼내어 그 종이에 적혀있는 값만큼 이동하여 다음 풍선을 터뜨린다. 양수가 적혀 있을 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동한다. 이동할 때에는 이미 터진 풍선은 빼고 이동한다.
#
# 예를 들어 다섯 개의 풍선 안에 차례로 3, 2, 1, -3, -1이 적혀 있었다고 하자. 이 경우 3이 적혀 있는 1번 풍선, -3이 적혀 있는 4번 풍선, -1이 적혀 있는 5번 풍선, 1이 적혀 있는 3번 풍선, 2가 적혀 있는 2번 풍선의 순서대로 터지게 된다.
#
#
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000)이 주어진다. 다음 줄에는 차례로 각 풍선 안의 종이에 적혀 있는 수가 주어진다. 종이에 0은 적혀있지 않다.
#
#
# 첫째 줄에 터진 풍선의 번호를 차례로 나열한다.

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
orders = list(map(int, input().split()))
balloons = deque((i+1, v) for i, v in enumerate(orders)) # 튜플 형식으로 deque에 저장

while balloons:
    count = balloons[0][1]
    i, v = balloons.popleft()
    print(i, end=" ")
    if balloons:
        if v > 0:
            for k in range(v-1):
                tmp = balloons.popleft()
                balloons.append(tmp)
        else:
            v = -v
            for k in range(v):
                tmp = balloons.pop()
                balloons.appendleft(tmp)
