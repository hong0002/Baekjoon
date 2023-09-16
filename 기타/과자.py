k, n, m = map(int, input().split())
sum = k*n
if sum - m > 0:
    print(sum-m)
else:
    print(0)
