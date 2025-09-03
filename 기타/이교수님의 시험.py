import sys

n = int(sys.stdin.readline().strip())
key = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

for i in range(1, n + 1):
    answers = list(map(int, sys.stdin.readline().split()))
    if answers == key:   # 만점자면 재시험 대상
        print(i)
