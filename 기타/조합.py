# nCm을 출력한다.
#
#
# n과 m이 주어진다. (5 ≤ n ≤ 100, 5 ≤ m ≤ 100, m ≤ n)
#
#
# nCm을 출력한다.

import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
print(math.factorial(n) // (math.factorial(n-m) * math.factorial(m)))
