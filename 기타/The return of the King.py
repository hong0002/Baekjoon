s = input().strip()
i = 0
total = 0
cnt = 0

while i < len(s):
    if s[i] == '1' and i + 1 < len(s) and s[i+1] == '0':
        total += 10
        cnt += 1
        i += 2
    else:
        total += int(s[i])
        cnt += 1
        i += 1

avg = total / cnt
print(f"{avg:.2f}")
