N = int(input().strip())

if N == 0:
    print("NO")
else:
    ok = True
    x = N
    while x > 0:
        if x % 3 == 2:
            ok = False
            break
        x //= 3
    print("YES" if ok else "NO")
