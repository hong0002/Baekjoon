import math
a, b, c = map(int, input().split())
print(max(math.trunc(a*b/c), math.trunc(a/b*c)))
