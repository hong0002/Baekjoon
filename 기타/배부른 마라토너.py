from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())

participants = [input().strip() for _ in range(N)]
finishers = [input().strip() for _ in range(N - 1)]

cnt = Counter(participants)

for name in finishers:
    cnt[name] -= 1

for name, count in cnt.items():
    if count > 0:
        print(name)
        break
