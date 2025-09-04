import sys

input = sys.stdin.readline
N = int(input().strip())

# S -> (D, C) (다음 풀리와 연결 유형)
next_edge = {}
for _ in range(N - 1):
    s, d, c = map(int, input().split())
    next_edge[s] = (d, c)

cur = 1
direction = 0  # 0=시계, 1=반시계
while cur != N:
    d, c = next_edge[cur]
    direction ^= c  # 교차(1)면 뒤집기
    cur = d

print(direction)
