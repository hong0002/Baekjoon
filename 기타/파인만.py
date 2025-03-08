while True:
    n = int(input())
    if n == 0:
        break
    result = n * (n + 1) * (2 * n + 1) // 6
    print(result)
