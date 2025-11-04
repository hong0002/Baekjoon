import sys, math

input = sys.stdin.readline
n = int(input().strip())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

g = 0
for ai, bi in zip(a, b):
    g = math.gcd(g, ai - bi)

print(g)
