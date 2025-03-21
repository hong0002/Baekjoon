a, b = map(int, input().split())
k, x = map(int, input().split())

start = max(a, k - x)
end = min(b, k + x)

if start > end:
    print("IMPOSSIBLE")
else:
    print(end - start + 1)
