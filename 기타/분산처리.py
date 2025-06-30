import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    r = pow(a, b, 10)
    print(10 if r == 0 else r)
