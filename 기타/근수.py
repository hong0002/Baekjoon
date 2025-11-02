import sys

input = sys.stdin.readline
N = int(input().strip())
S = input().strip()

ans = 0
cnt = 0
for ch in S:
    if ch == '2':
        cnt += 1
    else:
        if cnt:
            ans += cnt * (cnt + 1) * (cnt + 2) // 6
            cnt = 0
# 마지막 런 처리
if cnt:
    ans += cnt * (cnt + 1) * (cnt + 2) // 6

print(ans)
