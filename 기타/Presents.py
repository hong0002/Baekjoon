import sys

N = int(sys.stdin.readline().strip())
prices = []

for _ in range(N):
    s = sys.stdin.readline().strip()
    prices.append(float(s))

prices.sort()
second = prices[1]

# 소수 둘째 자리까지 출력
print(f"{second:.2f}")
