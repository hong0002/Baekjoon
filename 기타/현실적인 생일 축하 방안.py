import sys

input = sys.stdin.readline

B, N, M = map(int, input().split())

price = {}
for _ in range(N):
    name, p = input().split()
    price[name] = int(p)

total = 0
for _ in range(M):
    item = input().strip()
    total += price[item]

if total <= B:
    print("acceptable")
else:
    print("unacceptable")
