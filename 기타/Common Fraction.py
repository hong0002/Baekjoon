import sys
import math

def main():
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        g = math.gcd(a, b)
        print(a // g, b // g)

if __name__ == "__main__":
    main()
