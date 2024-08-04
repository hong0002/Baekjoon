# 입력 받기
X, Y = map(int, input().split())
N = int(input())

# 세븐25의 1000그램 당 가격 계산
seven25_price_per_1000g = (1000 / Y) * X

# 다른 편의점의 1000그램 당 가격 계산
min_price_per_1000g = seven25_price_per_1000g
for _ in range(N):
    Xi, Yi = map(int, input().split())
    price_per_1000g = (1000 / Yi) * Xi
    if price_per_1000g < min_price_per_1000g:
        min_price_per_1000g = price_per_1000g

# 최저가 출력 (소수점 둘째 자리까지)
print(f"{min_price_per_1000g:.2f}")
