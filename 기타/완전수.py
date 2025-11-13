import sys
import math

data = list(map(int, sys.stdin.read().split()))
T, nums = data[0], data[1:1+data[0]]

def classify(n: int) -> str:
    if n == 1:
        return "Deficient"  # 진약수 합 = 0
    s = 1  # 1은 항상 진약수(단, n>1일 때)
    r = int(math.isqrt(n))
    for d in range(2, r + 1):
        if n % d == 0:
            s += d
            q = n // d
            if q != d and q != n:
                s += q
    # 루트가 정확히 약수인 경우(d*d == n) 위에서 한 번만 더해짐
    # n 자체는 더하지 않음(진약수)
    if s == n:
        return "Perfect"
    elif s < n:
        return "Deficient"
    else:
        return "Abundant"

out = [classify(x) for x in nums]
print("\n".join(out))
