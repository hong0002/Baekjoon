import math

# 입력 받기
n = int(input())
a = list(map(int, input().split()))

# 숫자들을 오름차순으로 정렬
a.sort()

# 인접한 숫자들의 차이를 구함
differences = [a[i] - a[i - 1] for i in range(1, n)]

# 차이들의 GCD를 구함
m = differences[0]
for diff in differences[1:]:
    m = math.gcd(m, diff)

# k는 첫 번째 숫자 % m
k = a[0] % m

# 결과 출력
print(m, k)
