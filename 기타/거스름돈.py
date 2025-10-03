n = int(input().strip())

if n in (1, 3):
    print(-1)
else:
    r = n % 5
    q = n // 5
    if r == 0:
        print(q)
    elif r == 1:
        # n=1은 위에서 걸렀고, 나머지 1이면 5원 하나 줄이고 2원 3개
        print(q + 2)
    elif r == 2:
        print(q + 1)
    elif r == 3:
        # n=3은 위에서 걸렀고, 나머지 3이면 5원 하나 줄이고 2원 4개
        print(q + 3)
    else:  # r == 4
        print(q + 2)
