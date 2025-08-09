import sys

input = sys.stdin.readline
N = int(input().strip())
s = input().strip()

ans = 0
i = 0
while i < N:
    j = i
    # 같은 문자 run 확장
    while j < N and s[j] == s[i]:
        j += 1
    run_len = j - i
    if s[i] == 'a' and run_len >= 2:
        ans += run_len
    i = j

print(ans)
