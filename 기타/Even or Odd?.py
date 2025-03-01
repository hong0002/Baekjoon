n = int(input())
if n % 2 == 1:
    print(0)
else:
    k = n // 2
    if k % 2 == 0:
        print(2)
    else:
        print(1)
