a1, a0 = map(int, input().split())

c1, c2 = map(int, input().split())

n0 = int(input())

ok = (c1 <= a1 <= c2) and ((a1 - c1) * n0 + a0 >= 0) and ((a1 - c2) * n0 + a0 <= 0)

print(1 if ok else 0)
