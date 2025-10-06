N = int(input().strip())

if N == 1 or N == 2:
    print(1)
else:
    a, b = 1, 1  # F(1), F(2)
    for _ in range(3, N + 1):
        a, b = b, a + b  # F(n-1), F(n)
    print(b)
