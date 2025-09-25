def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

x = int(input().strip())
m = int(input().strip())

g, inv, _ = extended_gcd(x, m)

if g != 1:
    print("No such integer exists.")
else:
    # inv가 음수일 수 있으므로, m으로 나머지 연산
    inv = inv % m
    print(inv)
