s = input().strip()

ans = 1
for i in range(len(s)):
    if s[i] == 'c':
        if i > 0 and s[i-1] == 'c':
            ans *= 25
        else:
            ans *= 26
    else:  # 'd'
        if i > 0 and s[i-1] == 'd':
            ans *= 9
        else:
            ans *= 10

print(ans)
