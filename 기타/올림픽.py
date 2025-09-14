import sys

input = sys.stdin.readline
N, K = map(int, input().split())

medals = {}  # id -> (gold, silver, bronze)
for _ in range(N):
    i, g, s, b = map(int, input().split())
    medals[i] = (g, s, b)

gK, sK, bK = medals[K]

def better(a, b):
    # a가 b보다 더 잘했는지: 금 -> 은 -> 동 사전식 비교
    return a[0] > b[0] or (a[0] == b[0] and (a[1] > b[1] or (a[1] == b[1] and a[2] > b[2])))

cnt = sum(1 for v in medals.values() if better(v, (gK, sK, bK)))
print(cnt + 1)
