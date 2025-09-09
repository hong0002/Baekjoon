import sys
from math import gcd

def solve():
    data = sys.stdin.read().strip().split()
    n, a, b = map(int, data[:3])

    if gcd(a, b) != 1:
        print("No")
        return

    print("Yes")
    # (a+2ib, a+(2i+1)b)로 인접 원소 쌍을 출력
    for i in range(n):
        x = a + (2*i) * b
        y = x + b
        print(x, y)

if __name__ == "__main__":
    solve()
