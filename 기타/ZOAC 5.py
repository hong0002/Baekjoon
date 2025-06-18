import sys
s = sys.stdin.readline().rstrip()
c = s[0]
count = 0
for ch in s:
    if ch == c:
        count += 1
    else:
        break
print(count)
