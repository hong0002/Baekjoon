import sys

input = sys.stdin.readline
n = int(input().strip())
first_letters = set()

for _ in range(n):
    title = input().strip()
    if title:  # 안전 체크
        first_letters.add(title[0])

ans = 0
ch = ord('A')
while ch <= ord('Z') and chr(ch) in first_letters:
    ans += 1
    ch += 1

print(ans)
