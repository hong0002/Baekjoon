import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    prev = 0
    for ai in a:
        cand = prev + 1
        if cand == ai:
            cand += 1
        prev = cand
    print(prev)
