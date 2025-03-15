import sys
import math

# 입력 받기
input_data = sys.stdin.read().split()
n = int(input_data[0])
numbers = list(map(int, input_data[1:]))

# 최대공약수(GCD) 계산 함수
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# n개의 수에 대한 GCD 계산 (n이 2 또는 3)
if n == 2:
    g = gcd(numbers[0], numbers[1])
else:
    g = gcd(numbers[0], numbers[1])
    g = gcd(g, numbers[2])

# GCD의 약수 구하기
divisors = []
for i in range(1, int(math.sqrt(g)) + 1):
    if g % i == 0:
        divisors.append(i)
        if i != g // i:  # 중복되지 않게 추가
            divisors.append(g // i)

divisors.sort()

# 약수를 한 줄씩 출력
for d in divisors:
    print(d)
