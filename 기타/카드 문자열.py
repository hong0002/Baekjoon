from collections import deque

class Word:
    def __init__(self, data):
        self.data = data

t = int(input())
for _ in range(t):
    n = int(input())
    word = Word(deque(input().split()))
    result = deque()
    while word.data:
        current = word.data.popleft()
        if not result:
            result.append(current)
        else:
            if result[0] >= current: # 현재 알파벳이 맨 앞 알파벳보다 순서가 앞이라면
                result.appendleft(current)
            else:
                result.append(current)
    [print(i, end="") for i in result]
    print()
