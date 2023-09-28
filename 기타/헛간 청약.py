n, w, h, l = map(int, input().split())
a = w // l
b = h // l
if a*b > n:
    print(n)
else:
    print(a*b)
