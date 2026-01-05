import sys

s = sys.stdin.readline().strip()
n = len(s)

# right[i] = i 이상에서 시작하는 "))"의 개수
right = [0] * (n + 1)

for i in range(n - 2, -1, -1):
    right[i] = right[i + 1]
    if s[i] == ')' and s[i + 1] == ')':
        right[i] += 1

ans = 0
for i in range(n - 1):
    if s[i] == '(' and s[i + 1] == '(':
        ans += right[i + 1]  # y > i

print(ans)
