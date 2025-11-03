import sys

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

from collections import Counter

def odd_part(x: int) -> int:
    while x % 2 == 0:
        x //= 2
    return x

cnt = Counter(odd_part(x) for x in A)
print(max(cnt.values()))
