import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

ans = 0
cur = 0
for c in s:
    if c.isdigit():
        cur = cur * 10 + int(c)
    else:
        ans += cur
        cur = 0
# 마지막 남은 숫자 더하기
ans += cur

print(ans)
