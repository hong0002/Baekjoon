import sys

input = sys.stdin.readline
N = int(input().strip())
M = int(input().strip())
arr = list(map(int, input().split()))

arr.sort()
l, r = 0, N - 1
cnt = 0

while l < r:
    s = arr[l] + arr[r]
    if s == M:
        cnt += 1
        l += 1
        r -= 1
    elif s < M:
        l += 1
    else:
        r -= 1

print(cnt)
